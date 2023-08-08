from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def confirm_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_start = KeyboardButton('Все верно!')
    button_stop = KeyboardButton('Нет, выбрать заново.')
    keyboard.add(button_start, button_stop)
    return keyboard


