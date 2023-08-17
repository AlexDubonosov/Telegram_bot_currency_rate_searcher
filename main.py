
"""
Данный модуль запускает бот
"""

from telebot.custom_filters import StateFilter
import handlers
from database.models import create_models
from loader import bot
from units.menu import menu

if __name__ == '__main__':
    create_models()
    bot.add_custom_filter(StateFilter(bot))
    menu(bot)
    bot.infinity_polling()
