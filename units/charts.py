"""
Модуль для сохранения графика курса валюты за выбранный период
"""


import datetime

import matplotlib
import matplotlib.pyplot as plt

from config_data.config import currency_description
from units.twelve_date_from_list import twelve_date_from_list

# Исправляет ошибку UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail
matplotlib.use('agg')


def get_charts(data: list, time_period: list, user_currency: str) -> None:
    """
    Функция строит график на основе полученных данных и сохраняет его в виде изображения в основной директории.

    :param data: - значения курса выбранной валюты с определенным временным интервалом
    :param time_period: - период, за который собраны значения курса выбранной валюты
    :param user_currency: - название валюты
    :return:
    """

    # Повторяющиеся значения в ответе от api записываются как None, исправляем это, берем предыдущее значение.
    correct_data = []
    for index, value in enumerate(data):
        if value is None:
            value = data[index - 1]
            correct_data.append(value)
        else:
            correct_data.append(value)
    # размер графика
    plt.rcParams['figure.figsize'] = [10, 6]
    # строим график
    plt.plot([correct_data[key] for key in range(len(correct_data))], color='green')
    # подписи графика и осей
    if currency_description.get(user_currency):
        plt.title(f"Стоимость валюты: {currency_description[user_currency]}", fontsize=20)
    plt.ylabel('Стоимость')
    plt.xlabel('Выбранный диапазон дат')
    # значения оси X:
    # значений может быть от единиц до нескольких тысяч, сокращаем до +- 12, чтобы на графике это смотрелось органично
    short_time_period = twelve_date_from_list(time_period)
    short_time_period = [str(datetime.datetime.fromtimestamp(day)) for day in short_time_period]
    if len(time_period) > 12:
        shift = len(time_period) // 12
    else:
        shift = len(time_period)
    x_ticks = range(0, len(time_period), shift)
    plt.xticks(x_ticks, short_time_period, rotation=90)
    plt.tight_layout()
    # сохраняем полученный график
    plt.savefig('graf.png', dpi=300)
    # очистка текущего графического окна
    plt.clf()
