"""
Модуль предназначен для вызова календаря для выбора дат начала и конца периода,
а так же для обработки полученных дат и отправки запрошенного графика.
"""


import os

from telebot.types import ReplyKeyboardRemove, Message

from handlers.calendar.calendar import my_calendar_start
from loader import bot
from states.user_state import MyStates
from units import api


def calling_calendar(message: Message) -> None:
    """
    Функция вызывает первый календарь для ввода дат.

    :param message:
    :return:
    """
    bot.send_message(message.chat.id, 'Выберите даты', reply_markup=my_calendar_start())


@bot.message_handler(state=MyStates.next_date)
def send_chart_if_date_is_ready(message: Message) -> None:
    """
    Функция высылает пользователю график курсов валют по запрошенным им датам.

    :param message:
    :return:
    """
    remove_keyboard = ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Высылаю Вам запрошенный график, ожидайте:', reply_markup=remove_keyboard)
    api.print_charts(message.from_user.id)
    # Пробуем открыть созданный график, выводит предупреждение, если файл отсутствует.
    try:
        with open('graf.png', 'rb') as image:
            bot.send_photo(message.chat.id, image)
        os.remove('graf.png')
        bot.set_state(message.from_user.id, MyStates.not_state, message.chat.id)
    except FileNotFoundError:
        bot.set_state(message.from_user.id, MyStates.not_state, message.chat.id)
        print('Что-то пошло не так, график отсутствует!')
