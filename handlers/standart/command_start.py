from loader import bot
from telebot.types import Message
from states.user_state import MyStates
from peewee import IntegrityError
from database.db_with_orm import User


@bot.message_handler(commands=['start'])
def bot_start(message: Message):

    user_id = message.from_user.id
    user_first_name = message.from_user.first_name

    try:
        User.create(
            user_id=user_id,
            user_first_name=user_first_name,

        )
        bot.reply_to(message, f'Я Бот по поиску КУРСОВ ВАЛЮТ!'
                              'Ваша учетная запись создана,\n'
                              f'Добро пожаловать {user_first_name}')
    except IntegrityError:
        bot.reply_to(message, f'{user_first_name}, Вы уже зарегистрированы!')

    bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
    bot.send_message(message.chat.id, 'Как мне лучше к Вам обращаться? ')


@bot.message_handler(state=MyStates.name)
def name_write(message: Message):
    bot.send_message(message.chat.id, f'Договорились, {message.text}!\n'
                                      'Выберите интересующую Вас валюту: /currency\n'
                                      'Для дополнительной информации введите: /help.')
    bot.delete_state(message.from_user.id, message.chat.id)
