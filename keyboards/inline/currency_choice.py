from loader import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline import action_choice
from database import write_read_db


def currency_choice_keyboard():
    keyboard = InlineKeyboardMarkup()
    usd_button = InlineKeyboardButton('$ USD', callback_data='usd_button')
    eur_button = InlineKeyboardButton('€ EUR', callback_data='eur_button')
    btc_usd_button = InlineKeyboardButton('₿ BTC/USD', callback_data='btc_usd_button')
    other_button = InlineKeyboardButton('Остальные валюты', callback_data='other_button')
    keyboard.add(usd_button, eur_button)
    keyboard.add(btc_usd_button, other_button)
    return keyboard


@bot.callback_query_handler(func=lambda call:
                            call.data == 'usd_button' or
                            call.data == 'eur_button' or
                            call.data == 'btc_usd_button' or
                            call.data == 'other_button')
def callback_currency_choice(call):

    if call.data == 'usd_button':
        bot.send_message(call.message.chat.id, 'Выбрана валюта: USD')
        write_read_db.write_db('RUB=X', call.message.chat.id)

    elif call.data == 'eur_button':
        bot.send_message(call.message.chat.id, 'Выбрана валюта: EUR')
        write_read_db.write_db('EURRUB=X', call.message.chat.id)

    elif call.data == 'btc_usd_button':
        bot.send_message(call.message.chat.id, 'Выбрана валюта: BTC/USD')
        write_read_db.write_db('BTC-USD',call.message.chat.id)

    elif call.data == 'other_button':
        bot.send_message(call.message.chat.id, 'Введите символьный код необходимой валюты,\n'
                                               'либо воспользуйтесь /list для просмотра доступных кодов')

    bot.send_message(call.message.chat.id, 'Выберите действие:', reply_markup=action_choice.action_choice_keyboard())
