"""
Модуль для обработки любых текстовых сообщений не попавших под критерии описанные ранее.
"""

from telebot.types import Message

from loader import bot


@bot.message_handler(content_types=['text'])
def other_commands_handler(message: Message) -> None:
    """
    Функция срабатывает при получении текстового сообщения, которое не смогли обработать хендлеры ранее.

    :param message:
    :return:
    """

    bot.send_message(message.chat.id, 'К сожалению я не распознал вашу команду,\n'
                                      'пожалуйста, повторите ввод либо воспользуйтесь '
                                      '/help или меню.')
