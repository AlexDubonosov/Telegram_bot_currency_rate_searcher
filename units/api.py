from config_data import config
import json
import requests
from units.find_key_in_json import find_keys_in_json
from database.write_read_db import read_db


# Данные вашего API
user_api_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/"
user_api_headers = {
    "X-RapidAPI-Key": config.API_KEY,
    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
}


# GET/POST запросы к API для получения десериализованного json
def api_request(method_endswith, params, method_type):
    url = f"{user_api_url}{method_endswith}"
    if method_type == 'GET':
        return get_request(url=url, params=params)
    else:
        return post_request(url=url, params=params)


def get_request(url, params):
    try:
        response = requests.get(
            url,
            headers=user_api_headers,
            params=params,
            timeout=15
        )
        if response.status_code == requests.codes.ok:
            return json.loads(response.text)
    except Exception as err_text:
        print('Что-то пошло не так:')
        print(err_text)


# Пока нет post запросов
def post_request(url, params):
    pass


# Поиск стоимости выбранной валюты
def chosen_currency_price(key):
    user_data_from_db = read_db()
    user_currency = find_keys_in_json(user_data_from_db, 'currency')
    data = api_request(method_endswith='market/v2/get-quotes',
                       params={"region": "US", "symbols": user_currency},
                       method_type='GET')

    value = find_keys_in_json(data, key)
    return value

