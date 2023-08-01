import json
import os


user = {}


def write_db(data):
    with open(os.path.abspath(os.path.join('database', f'{user["name"]}{user["chat_id"]}.json')), 'w', encoding='utf8') as file:
        user_info = {user['name']: {
            'chat_id': user["chat_id"],
            'currency': data
        }}
        json.dump(user_info, file)


def read_db():
    with open(os.path.abspath(os.path.join('database', f'{user["name"]}{user["chat_id"]}.json')), 'r') as file:
        data = json.load(file)
        return data
