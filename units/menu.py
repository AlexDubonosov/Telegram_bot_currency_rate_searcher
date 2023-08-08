from telebot.types import BotCommand
from config_data.config import MENU_COMMANDS


def menu(bot):
    bot.set_my_commands([BotCommand(*i) for i in MENU_COMMANDS])
