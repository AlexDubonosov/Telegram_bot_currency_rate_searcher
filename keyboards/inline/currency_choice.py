from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def currency_choice_keyboard():
    keyboard = InlineKeyboardMarkup()
    usd_button = InlineKeyboardButton('$ USD', callback_data='usd_button')
    eur_button = InlineKeyboardButton('€ EUR', callback_data='eur_button')
    btc_usd_button = InlineKeyboardButton('₿ BTC/USD', callback_data='btc_usd_button')
    gold_button = InlineKeyboardButton('[Au] Gold', callback_data='gold_button')
    index500_button = InlineKeyboardButton('S&P 500', callback_data='index500_button')
    yuan_button = InlineKeyboardButton('¥ Yuan', callback_data='yuan_button')
    yen_button = InlineKeyboardButton('¥ Yen', callback_data='yen_button')
    other_button = InlineKeyboardButton('Остальные валюты', callback_data='other_button')

    keyboard.add(usd_button, eur_button, btc_usd_button)
    keyboard.add(gold_button, index500_button)
    keyboard.add(yuan_button, yen_button)
    keyboard.add(other_button)

    return keyboard

