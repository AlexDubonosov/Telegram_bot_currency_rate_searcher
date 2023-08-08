from loader import bot
from telebot.types import Message
from keyboards.inline import currency_choice


@bot.message_handler(commands=['currency'])
def choice_currency(message: Message):
    bot.send_message(message.chat.id, 'Выберите валюту:',
                     reply_markup=currency_choice.currency_choice_keyboard())










