from loader import bot
from telebot.types import Message
from units import api


@bot.message_handler(commands=['low'])
def get_low(message: Message):
    result = api.return_value_from_api('regularMarketDayLow')
    bot.send_message(message.chat.id, f'regularMarketDayLow - {result}')


