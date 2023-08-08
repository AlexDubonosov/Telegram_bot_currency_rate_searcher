from handlers.calendar.calendar import my_calendar_start
from database.write_read_db import clear_date
from states.user_state import MyStates
import os
from loader import bot
from units import api
from telebot.types import ReplyKeyboardRemove


def change_date_state(message):
    bot.send_message(message.chat.id, 'Выберите даты', reply_markup=my_calendar_start(message))


@bot.message_handler(state=MyStates.next_date)
def send_chart_if_date_is_ready(message):
    remove_keyboard = ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Высылаю Вам запрошенный график, ожидайте:', reply_markup=remove_keyboard)
    api.print_charts(message.chat.id)
    with open('graf.png', 'rb') as image:
        bot.send_photo(message.chat.id, image)
    os.remove('graf.png')
    clear_date(message.chat.id)
    bot.delete_state(message.from_user.id, message.chat.id)
