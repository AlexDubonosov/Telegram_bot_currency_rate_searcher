"""
Модуль предназначен для обработки ручного ввода валюты пользователем
"""

from loader import bot
from states.user_state import MyStates
from database.db_with_orm import write_currency_in_db
from keyboards.inline.action_choice import action_choice_keyboard
from telebot.types import Message


@bot.message_handler(state=MyStates.input_currency)
def write_user_currency_in_db(message: Message) -> None:
    """
    Функция срабатывает при установке состояния input_currency.
    Получает на вход данные от пользователя, записывает валюту в БД
    и вызывает клавиатуру для выбора интересующего курса.

    :param message:
    :return:
    """
    user_currency = message.text
    write_currency_in_db(message.from_user.id, user_currency)
    bot.send_message(message.chat.id, 'Какой курс вас интересует:',
                     reply_markup=action_choice_keyboard())
