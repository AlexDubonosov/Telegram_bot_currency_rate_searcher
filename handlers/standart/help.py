from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['help'])
def bot_help(message: Message) -> None:
    bot.send_message(message.chat.id, 'В боте доступны следующие команды:\n'
                                      '/currency - выбор валюты и интересующих значений'
                                      '/history - история последних запросов\n'
                     )