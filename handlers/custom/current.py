from loader import bot
from telebot.types import Message
from units import api


@bot.message_handler(commands=['current'])
def get_current(message: Message):
    result = api.return_value_from_api('regularMarketPrice')
    bot.send_message(message.chat.id, f'regularMarketPrice - {result}')


