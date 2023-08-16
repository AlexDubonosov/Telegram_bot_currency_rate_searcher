"""
Модуль для проверки правильности введенных дат
"""

import datetime


def check_date(date_period: str) -> bool:
    """
    Функция проверяет правильность введенных дат

    :param date_period:
    :return: - возвращает True, если даты корректны, и False, если нет
    """
    y, m, d = date_period[0].split('-')
    start_time = datetime.datetime(int(y), int(m), int(d))

    y, m, d = date_period[1].split('-')
    end_time = datetime.datetime(int(y), int(m), int(d))

    print(start_time, end_time)

    if start_time >= end_time:
        return False
    return True
