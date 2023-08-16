
"""
Модуль для хранения всех функций обращения к базе данных
"""

from database.models import Currency, User


def create_user(user_id: int, user_first_name: str) -> bool:
    """
    Функция создает запись о пользователе в БД если его нет и возвращает True,
    если пользователь уже есть - возвращает False.

    :param user_id: - id пользователя в чате
    :param user_first_name: - имя пользователя в ТГ
    :return: - True или False
    """
    person, created = User.get_or_create(user_id=user_id, user_first_name=user_first_name)
    if person:
        return False
    return True


def write_currency_in_db(user_id: int, currency: str) -> None:
    """
    Записывает в БД какую валюту выбрал пользователь.

    :param user_id: - id пользователя в чате
    :param currency: - строка с названием валюты
    :return: - None
    """
    Currency(
        user=user_id,
        currency=currency
    ).save()


def write_date_period_in_db_in_last_slot_for_user(user_id: int, date_period: dict) -> None:
    """
    Функция записывает выбранные даты для построения графика в БД.
    1. Ищем последнюю строку для конкретного пользователя
    2. Ячейке date_period приравниваем выбранные даты
    3. Записываем даты в БД

    :param user_id: - id пользователя в чате
    :param date_period: - словарь, [0]- дата начала периода, [1] - дата конца периода
    :return: - None
    """

    last_entry = Currency.select().where(Currency.user_id == user_id).order_by(Currency.id.desc()).first()
    last_entry.date_period = date_period['date_period'][0] + " " + date_period['date_period'][1]
    last_entry.save()


def read_currency_for_user(user_id: int) -> str:
    """
    Функция обращается к БД, ищет последнюю строку для пользователя и считывает ячейку с названием валюты.

    :param user_id: - id пользователя в чате
    :return: - строковое представление названия валюты
    """
    currency = Currency.select().where(Currency.user_id == user_id).order_by(Currency.id.desc()).first().currency
    return currency


def read_date_for_user(user_id: int) -> str:
    """
    Функция обращается к БД, ищет последнюю строку для пользователя и считывает ячейку датами начала и конца периода.

    :param user_id: - id пользователя в чате
    :return: - строковое представление дат начала и конца периода для построения графика
    """
    date_period = Currency.select().where(Currency.user_id == user_id).order_by(Currency.id.desc()).first().date_period
    return date_period
