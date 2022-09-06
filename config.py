from os import environ as env
from dotenv import load_dotenv
import json
load_dotenv()


settings = {
    'token': env["TOKEN_BOT"],
    'bot': 'Прабабка',
    'prefix': '/'
}

settings_db = {
    'host': env['HOST_DB'],
    'port': int(env['PORT_DB']),
    'name_db': env['NAME_DB'],
    'collect_ds': env['COLLECT_DS'],
    'collect_users': env['COLLECT_USERS']
}
