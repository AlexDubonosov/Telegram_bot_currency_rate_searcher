from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def action_choice_keyboard():
    keyboard = InlineKeyboardMarkup()
    current_button = InlineKeyboardButton('➡️ now', callback_data='current_button')
    low_button = InlineKeyboardButton('⬇️ min', callback_data='low_button')
    high_button = InlineKeyboardButton('⬆️ max', callback_data='high_button')
    custom_button = InlineKeyboardButton('График за указанный период', callback_data='custom_button')
    keyboard.add(current_button, low_button, high_button)
    keyboard.add(custom_button)
    return keyboard

