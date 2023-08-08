import json
import os


def create_needed_files(chat_id):

    if os.path.exists(os.path.abspath(os.path.join('database', f'currency_{chat_id}.json'))) is False:
        with open(os.path.abspath(os.path.join('database', f'currency_{chat_id}.json')), 'w', encoding='utf8') as file:
            user_info = {'currency': None}
            json.dump(user_info, file)

    if os.path.exists(os.path.abspath(os.path.join('database', f'date_{chat_id}.json'))) is False:
        with open(os.path.abspath(os.path.join('database', f'date_{chat_id}.json')), 'w', encoding='utf8') as file:
            user_info = {'date': []}
            json.dump(user_info, file)

    if os.path.exists(os.path.abspath(os.path.join('database', f'history_{chat_id}.json'))) is False:
        with open(os.path.abspath(os.path.join('database', f'history_{chat_id}.json')), 'w', encoding='utf8') as file:
            user_info = {'history': None}
            json.dump(user_info, file)


def write_currency(currency, chat_id):
    with open(os.path.abspath(os.path.join('database', f'currency_{chat_id}.json')), 'w', encoding='utf8') as file:
        user_info = {'currency': currency}
        json.dump(user_info, file)


def read_currency(chat_id):
    with open(os.path.abspath(os.path.join('database', f'currency_{chat_id}.json')), 'r') as file:
        data = json.load(file)
        return data


def write_date(user_date, chat_id):
    with open(os.path.abspath(os.path.join('database', f'date_{chat_id}.json')), 'r', encoding='utf8') as file:
        date_period = json.load(file)
        date_period['date'].append(user_date)
    with open(os.path.abspath(os.path.join('database', f'date_{chat_id}.json')), 'w', encoding='utf8') as file:
        json.dump(date_period, file)


def clear_date(chat_id):
    with open(os.path.abspath(os.path.join('database', f'date_{chat_id}.json')), 'w', encoding='utf8') as file:
        date_period = {'date': []}
        json.dump(date_period, file)


def check_date(chat_id):
    with open(os.path.abspath(os.path.join('database', f'date_{chat_id}.json')), 'r', encoding='utf8') as file:
        date_period = json.load(file)
        print(date_period['date'])
        if len(date_period['date']) == 2:
            return True
        else:
            return False


def read_date(chat_id):
    with open(os.path.abspath(os.path.join('database', f'date_{chat_id}.json')), 'r') as file:
        data = json.load(file)
        return data


def write_history():
    pass


def read_history():
    pass
