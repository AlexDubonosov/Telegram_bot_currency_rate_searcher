import json
import os


user = {}


def write_db(data, chat_id):
    with open(os.path.abspath(os.path.join('database', f'{user["name"]}{chat_id}.json')), 'w', encoding='utf8') as file:
        user_info = {user['name']: {
            'currency': data,
            'history': None
        }}
        json.dump(user_info, file)


def read_db(chat_id):
    with open(os.path.abspath(os.path.join('database', f'{user["name"]}{chat_id}.json')), 'r') as file:
        data = json.load(file)
        return data
