import pprint

from config_data import config
import json
import requests
from units.find_key_in_json import find_keys_in_json
from database.write_read_db import read_currency
from units.convert_date import convert_date
from units.charts import get_charts

# Данные вашего API
user_api_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/"
user_api_headers = {
    "X-RapidAPI-Key": config.API_KEY,
    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
}


# GET/POST запросы к API для получения десериализованного json
def api_request(method_endswith: str, params: dict, method_type: str) -> [dict, None]:
    url = f"{user_api_url}{method_endswith}"
    if method_type == 'GET':
        return get_request(url=url, params=params)
    else:
        return post_request(url=url, params=params)


def get_request(url: str, params: dict) -> dict:
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
    return None


# Поиск стоимости выбранной валюты
def chosen_currency_price(key: str, chat_id: str) -> str:
    user_currency_from_db = read_currency(chat_id)
    user_currency = find_keys_in_json(user_currency_from_db, 'currency')
    print(user_currency)
    data = api_request(method_endswith='market/v2/get-quotes',
                       params={"region": "US", "symbols": user_currency},
                       method_type='GET')
    value = find_keys_in_json(data, key)
    # Перевод курса золота из доллара за унцию в рубли за грамм
    if user_currency == ['GC=F, RUB=X']:
        result = round(value[0] * value[1] / 31.10, 3)
        return result
    else:
        return value[0]  # [0] возвращается т.к. для золота ищем сразу 2 курса, а для остальных валют нужен 1


# Вывод графика курса валюты за выбранный период
def print_charts(chat_id: str) -> None:
    user_currency_from_db = read_currency(chat_id)
    user_currency = find_keys_in_json(user_currency_from_db, 'currency')
    interval, start_time, end_time = convert_date(chat_id)
    data = api_request(method_endswith='stock/v2/get-chart',
                       params={"interval": interval, "symbol": user_currency, "region": "US", "period1": start_time, "period2": end_time},
                       method_type='GET')
    # pprint.pprint(data)
    value = find_keys_in_json(data, 'open')[0]
    time_period = find_keys_in_json(data, 'timestamp')[0]
    get_charts(value, time_period, user_currency)



