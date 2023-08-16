"""
Модуль содержащий описание пользовательских состояний
"""

from telebot.handler_backends import State, StatesGroup


class MyStates(StatesGroup):
    """
    Класс для смены состояний при опросе пользователя
    """
    name = State()
    input_currency = State()
    next_date = State()
    not_state = State()
