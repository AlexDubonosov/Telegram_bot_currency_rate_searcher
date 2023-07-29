from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['help'])
def bot_help(message: Message) -> None:
    bot.send_message(message.chat.id, 'В боте доступны следующие команды:\n'
                                      '/current - текущий курс\n'
                                      '/low - вывод минимального курса за день\n'
                                      '/high - вывод максимального курса за день\n'
                                      '/custom - вывод курса за указанный период(календарь)\n'
                                      '/history - история последних запросов\n'
                     )