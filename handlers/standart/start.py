from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['start'])
def bot_start(message: Message) -> None:
    bot.send_message(message.chat.id, f'Привет! Я Бот по поиску КУРСОВ ВАЛЮТ, добро пожаловать {message.from_user.first_name}!\n'
                                      f'Для начала выберите валюту: /currency\n'
                                      f'Введите /help для информации по возможным командам.'
                     )
