"""
Модуль для обработки команды /history
"""

from loader import bot
from telebot.types import Message
from database.models import Currency, User
from telebot.types import List
from config_data.config import currency_description


@bot.message_handler(commands=['history'])
def currency_history(message: Message) -> None:
    """
    Функция обрабатывает команду /history, обращается к БД и отправляет пользователю последние 10 запрошенных им валют.

    :param message:
    :return:
    """
    bot.send_message(message.chat.id, 'Последние 10 запрошенных валют:')
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)
    history: List[Currency] = user.history.order_by(-Currency.id).limit(10)
    result = [currency_description[text.currency] for text in history[-1::-1]]
    bot.send_message(message.chat.id, '\n'.join(result))
