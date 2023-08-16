"""
Модуль для обработки команды /help
"""


from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['help'])
def bot_help(message: Message) -> None:
    """
    При получении команды /help выводится подсказка.

    :param message:
    :return:
    """
    bot.send_message(message.chat.id, 'В боте доступны следующие команды:\n\n'
                                      '/currency - выбор валюты и ее значений: '
                                      'Вы можете запросить минимальную, максимальную и текущую стоимость,'
                                      'а так же график за какой-либо определенный период.\n\n'
                                      '/history - последние 10 просмотренных валют\n\n'
                                      'Все доступные кнопки так же можно найти в Menu'
                     )