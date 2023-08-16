"""
Модуль для создания кнопки MENU
"""


from telebot.types import BotCommand
from config_data.config import MENU_COMMANDS


def menu(bot) -> None:
    """
    Функция создает кнопку menu со списком команд.

    :param bot:
    :return:
    """
    bot.set_my_commands([BotCommand(*i) for i in MENU_COMMANDS])
