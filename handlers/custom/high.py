from loader import bot
from telebot.types import Message
from units import api


@bot.message_handler(commands=['high'])
def get_high(message: Message):
    result = api.return_value_from_api('regularMarketDayHigh')
    bot.send_message(message.chat.id, f'regularMarketDayHigh - {result}')


