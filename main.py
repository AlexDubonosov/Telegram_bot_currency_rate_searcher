from loader import bot
import handlers
from telebot.custom_filters import StateFilter
from units.menu import menu


if __name__ == '__main__':
    bot.add_custom_filter(StateFilter(bot))
    menu(bot)
    bot.infinity_polling()
