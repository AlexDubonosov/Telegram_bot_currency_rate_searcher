from loader import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from units import api


def action_choice_keyboard():
    keyboard = InlineKeyboardMarkup()
    current_button = InlineKeyboardButton('➡️ Текущее значение', callback_data='current_button')
    low_button = InlineKeyboardButton('⬇️ Минимальное за день', callback_data='low_button')
    high_button = InlineKeyboardButton('⬆️ Максимальное за день', callback_data='high_button')
    custom_button = InlineKeyboardButton('График за указанный период', callback_data='custom_button')
    keyboard.add(low_button, high_button)
    keyboard.add(current_button, custom_button)
    return keyboard


@bot.callback_query_handler(func=lambda call:
                            call.data == 'current_button' or
                            call.data == 'low_button' or
                            call.data == 'high_button' or
                            call.data == 'custom_button')
def callback_action_choice(call):
    if call.data == 'current_button':
        result = api.chosen_currency_price('regularMarketPrice', call.message.chat.id)
        bot.send_message(call.message.chat.id, f'Текущая стоимость:  {result}')

    elif call.data == 'low_button':
        result = api.chosen_currency_price('regularMarketDayLow', call.message.chat.id)
        bot.send_message(call.message.chat.id, f'Минимальная цена за день:  {result}')

    elif call.data == 'high_button':
        result = api.chosen_currency_price('regularMarketDayHigh', call.message.chat.id)
        bot.send_message(call.message.chat.id, f'Максимальная цена за день:  {result}')

    elif call.data == 'custom_button':
        bot.send_message(call.message.chat.id, 'красивый график', call.message.from_user.first_name)
