"""
Модуль для работы с API.
Используется API https://rapidapi.com/apidojo/api/yahoo-finance1
"""


import json

import requests

from config_data import config
from database.db_with_orm import read_date_for_user, read_currency_for_user
from loader import bot
from units.charts import get_charts
from units.convert_date import convert_date
from units.find_key_in_json import find_keys_in_json

# Данные вашего API
user_api_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/"
user_api_headers = {
    "X-RapidAPI-Key": config.API_KEY,
    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
}


# GET/POST запросы к API для получения десериализованного json
def api_request(method_endswith: str, params: dict, method_type: str) -> [dict, None]:
    """
    Универсальная функция для отправки get или post запросов.
    Содержит необходимые параметры для обращения к API:

    :param method_endswith: - endpoint к которому идет обращение
    :param params: - словарь, содержащий API ключ и url
    :param method_type: get или post
    :return: словарь из полученного от api json либо None
    """

    url = f"{user_api_url}{method_endswith}"
    if method_type == 'GET':
        return get_request(url=url, params=params)
    else:
        return post_request(url=url, params=params)


def get_request(url: str, params: dict) -> [dict, None]:
    """
    Функция делающая GET запрос.

    :param url:
    :param params:
    :return:
    """
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
    """
    Функция делающая POST запрос.
    Не используется.

    :param url:
    :param params:
    :return:
    """
    return None


def chosen_currency_price(key: str, user_id: int, key2=None) -> [str, tuple]:
    """
    Функция делающая GET запрос к API для получения стоимости валюты.

    :param key: - необходимый курс
    :param user_id: - id пользователя, делающего запрос
    :param key2: - необязательный параметр, используется при запросе текущего курса для отображения разницы
    в стоимости валюты на начало дня
    :return: может вернуть как одно значение в виде строки, так и кортеж из нескольких значений(для золота)
    """
    user_currency = read_currency_for_user(user_id)
    data = api_request(method_endswith='market/v2/get-quotes',
                       params={"region": "US", "symbols": user_currency},
                       method_type='GET')
    value = find_keys_in_json(data, key)
    if key2 is not None:
        value_change = find_keys_in_json(data, key2)
    # Перевод курса золота из доллара за унцию в рубли за грамм (по просьбе друга XD)
    if user_currency == 'GC=F, RUB=X':
        result = round(value[0] * value[1] / 31.10, 3)
        return result
    else:
        try:
            if key2 is not None:
                return value[0], value_change[0]
            else:
                return value[0]  # [0] возвращается т.к. для золота ищем сразу 2 курса, а для остальных валют нужен 1
        except IndexError:
            bot.send_message(user_id, 'Я получил некоррекные данные, возможно выбранная '
                                      'Вами валюта некорректно введена или не существует. '
                                      'Попробуйте еще раз, нажав /currency')


def print_charts(user_id: int) -> None:
    """
    Функция делающая GET запрос к API для вывода графика курса валюты за выбранный период
    :param user_id:
    :return:
    """
    user_currency = read_currency_for_user(user_id)
    user_date_period = read_date_for_user(user_id)
    interval, start_time, end_time = convert_date(user_date_period)
    data = api_request(method_endswith='stock/v2/get-chart',
                       params={"interval": interval, "symbol": user_currency, "region": "US", "period1": start_time, "period2": end_time},
                       method_type='GET')

    try:
        value = find_keys_in_json(data, 'open')[0]
        time_period = find_keys_in_json(data, 'timestamp')[0]
        get_charts(value, time_period, user_currency)
    except IndexError:
        bot.send_message(user_id, 'Я получил некоррекные данные, возможно выбранная '
                                  'Вами валюта некорректно введена или не существует.\n'
                                  'Попробуйте еще раз, нажав /currency')




