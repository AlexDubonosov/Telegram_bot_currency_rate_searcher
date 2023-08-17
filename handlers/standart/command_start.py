"""
Модуль для обработки команды /start
"""


from telebot.types import Message

from database.db_with_orm import create_user
from loader import bot
from states.user_state import MyStates


@bot.message_handler(commands=['start'])
def bot_start(message: Message) -> None:
    """
    При получении команды /start выводится сообщение знакомящее с ботом.
    Если пользователь не существует, то его данные записываются в БД, если уже существует,
    выводится соответствующее приветствие.

    :param message:
    :return:
    """
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user = create_user(user_id, user_first_name)
    if user:
        bot.reply_to(message, f'Я Бот по поиску КУРСОВ ВАЛЮТ!\n'
                              'Ваша учетная запись создана,\n'
                              f'Добро пожаловать {user_first_name}')
    else:
        bot.reply_to(message, f'{user_first_name}, Вы уже зарегистрированы!')

    bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
    bot.send_message(message.chat.id, 'Как мне лучше к Вам обращаться? ')


@bot.message_handler(state=MyStates.name)
def name_write(message: Message) -> None:
    """
    Функция обрабатывает состояние name для обработки введенного пользователем имени(не используется).

    :param message:
    :return:
    """
    bot.send_message(message.chat.id, f'Договорились, {message.text}!\n'
                                      'Выберите интересующую Вас валюту: /currency\n'
                                      'Для дополнительной информации введите: /help.')
    bot.delete_state(message.from_user.id, message.chat.id)
