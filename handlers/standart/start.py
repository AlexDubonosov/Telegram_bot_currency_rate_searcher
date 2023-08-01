from loader import bot
from telebot.types import Message
from states.user_state import MyStates
from database.write_read_db import user


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
    bot.send_message(
        message.chat.id, f'Добро пожаловать!\n'
                         f'Я Бот по поиску КУРСОВ ВАЛЮТ!'
                         '\n\n'
                         'Давайте познакомимся! Напишите свое имя: '
                     )


@bot.message_handler(state=MyStates.name)
def name_write(message: Message):
    user['name'] = message.from_user.id
    user['chat_id'] = message.chat.id
    bot.send_message(message.chat.id, f'Привет, {message.text}!\n'
                                      f'Чтобы начать выберите валюту: /currency\n'
                                      f'Для дополнительной информации введите: /help.')
