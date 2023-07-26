import os
import telebot
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(token)

# примеры обработки команд
@bot.message_handler(commands=['start', 'stop'])
def handle_start_stop_commands(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Hi! Im your bot, nice to see you!')
        bot.send_message(message.chat.id, 'Menu:\n'
                                          '/start\n'
                                          '/stop\n'
                                          '/keyboard\n'
                         )
    elif message.text == '/stop':
        bot.send_message(message.chat.id, 'Bye!')
    else:
        bot.send_message(message.chat.id, 'I do not know this command!')


# примеры ответа на полученную инфу
@bot.message_handler(commands=['name'])
def handle_name(message):
    bot.send_message(message.chat.id, 'How is your name?')
    bot.register_next_step_handler(message, process_name)


def process_name(message):
    name = message.text
    bot.send_message(message.chat.id, f'Hi, {name}')


# примеры примеры простых кнопок
@bot.message_handler(commands=['keyboard'])
def handle_keyboard(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_start = telebot.types.KeyboardButton('/start')
    button_stop = telebot.types.KeyboardButton('/stop')
    button_name = telebot.types.KeyboardButton('/name')
    button_inl_keyboard = telebot.types.KeyboardButton('/inline_keyboard')
    button_remove = telebot.types.KeyboardButton('/remove_keyboard')
    keyboard.add(button_start, button_stop,button_name)
    keyboard.add(button_inl_keyboard, button_remove)
    bot.send_message(message.chat.id, 'Choice button:', reply_markup=keyboard)

# примеры инлайн кнопок
@bot.message_handler(commands=['inline_keyboard'])
def handle_inline_keyboard(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton('first', callback_data='button_first')
    button_second = telebot.types.InlineKeyboardButton('second', callback_data='button_second')

    keyboard.add(button_first)
    keyboard.add(button_second)

    bot.send_message(message.chat.id, "Нажми на кнопку:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'button_first':
        bot.send_message(call.message.chat.id, 'You pressed first button')
    elif call.data == 'button_second':
        bot.send_message(call.message.chat.id, 'You pressed second button')

    bot.answer_callback_query(callback_query_id=call.id, text='Pressed')


# удаление клавиатуры
@bot.message_handler(commands=['remove_keyboard'])
def handle_remove_keyboard(message):
    keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Keyboard was deteted', reply_markup=keyboard)


# примеры реакции на текст/либо что-то еще
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.lower() in ['привет', 'даров', 'хай', 'здорова', 'hi', 'hello']:
        bot.send_message(message.chat.id, "Hi, what's up?")
    else:
        bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling()
