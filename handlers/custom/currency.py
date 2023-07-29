from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['currency'])
def choice_currency(message: Message):
    user_currency = bot.send_message(message.chat.id, 'Выберите валюту(стоимость по отношению к рублю):\n'
                                                      '"RUB=X"\n'
                                                      '"EURRUB=X"\n'
                                                      '"BTC-USD"\n'
                                     )
    bot.register_next_step_handler(user_currency, write_currency)


def write_currency(message: Message):
    user_currency = message.text
    with open('E:\python\skillbox\python_basic_diploma\database\current_currency.txt', 'w') as file:
        file.write(user_currency)
    bot.send_message(message.chat.id, f'Выбрана валюта {user_currency}')


