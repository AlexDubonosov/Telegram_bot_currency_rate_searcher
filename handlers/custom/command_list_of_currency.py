"""
Модуль для обработки команды /list
"""

from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['list'])
def list_of_currency(message: Message) -> None:
    """
    Функция обрабатывает команду /list и отправляет пользователю список валют, которые он может ввести вручную.

    :param message:
    :return:
    """

    currency = "GBPRUB=X : Британский фунт стерлингов (GBP) к российскому рублю (RUB).\n" \
               "AUDRUB=X : Австралийский доллар (AUD) к российскому рублю (RUB).\n" \
               "CADRUB=X : Канадский доллар (CAD) к российскому рублю (RUB).\n" \
               "CHFRUB=X : Швейцарский франк (CHF) к российскому рублю (RUB).\n" \
               "SEKRUB=X : Шведская крона (SEK) к российскому рублю (RUB).\n" \
               "NZDRUB=X : Новозеландский доллар (NZD) к российскому рублю (RUB).\n" \
               "SGBRUB=X : Сингапурский доллар (SGD) к российскому рублю (RUB).\n" \
               "HKDRUB=X : Гонконгский доллар (HKD) к российскому рублю (RUB).\n" \
               "NOKRUB=X : Норвежская крона (NOK) к российскому рублю (RUB).\n" \
               "KRWRUB=X : Южнокорейская вона (KRW) к российскому рублю (RUB).\n" \
               "TRYRUB=X : Турецкая лира (TRY) к российскому рублю (RUB).\n" \
               "INRRUB=X : Индийская рупия (INR) к российскому рублю (RUB).\n" \
               "BRLRUB=X : Бразильский реал (BRL) к российскому рублю (RUB).\n" \
               "ZARRUB=X : Южноафриканский рэнд (ZAR) к российскому рублю (RUB).\n" \
               "MXNRUB=X : Мексиканское песо (MXN) к российскому рублю (RUB).\n"

    bot.send_message(message.chat.id, currency)
