"""
Модуль для обработки инлайн клавиатур
"""


from telebot.types import CallbackQuery

from database.db_with_orm import write_currency_in_db
from handlers.custom.calling_calendar import calling_calendar
from keyboards.inline.action_choice import action_choice_keyboard
from loader import bot
from states.user_state import MyStates
from units.api import chosen_currency_price


@bot.callback_query_handler(func=lambda call:
                            call.data == 'current_button' or
                            call.data == 'low_button' or
                            call.data == 'high_button' or
                            call.data == 'custom_button')
def callback_action_choice(call: CallbackQuery) -> None:
    """
    Функция ловит нажатия инлайн кнопок для выбора определенного курса выбранной валюты.

    :param call:
    :return:
    """
    stripe = '-' * 50

    if call.data == 'current_button':
        result = chosen_currency_price('regularMarketPrice', call.from_user.id, 'regularMarketChange')
        if isinstance(result, tuple):
            if result[1] is not None:
                if result[1] > 0:
                    bot.send_message(call.message.chat.id, f'{stripe}\nТекущая стоимость:\n{result[0]} '
                                                           f'+{round(result[1], 3)}\n{stripe}')
                else:
                    bot.send_message(call.message.chat.id, f'{stripe}\nТекущая стоимость:\n{result[0]} '
                                                           f'{round(result[1], 3)}\n{stripe}')
        else:
            if result is not None:
                bot.send_message(call.message.chat.id, f'{stripe}\nТекущая стоимость:\n{result}\n{stripe}')

    elif call.data == 'low_button':
        result = chosen_currency_price('regularMarketDayLow', call.from_user.id)
        if result is not None:
            bot.send_message(call.message.chat.id, f'{stripe}\nМинимальная цена за день:\n{result}\n{stripe}')

    elif call.data == 'high_button':
        result = chosen_currency_price('regularMarketDayHigh', call.from_user.id)
        if result is not None:
            bot.send_message(call.message.chat.id, f'{stripe}\nМаксимальная цена за день:\n{result}\n{stripe}')

    elif call.data == 'custom_button':
        calling_calendar(call.message)


# user_storage = {}


@bot.callback_query_handler(func=lambda call:
                            call.data == 'usd_button' or
                            call.data == 'eur_button' or
                            call.data == 'btc_usd_button' or
                            call.data == 'gold_button' or
                            call.data == 'sber_usd_button' or
                            call.data == 'index500_button' or
                            call.data == 'yuan_button' or
                            call.data == 'yen_button')
def callback_currency_choice(call: CallbackQuery) -> None:
    """
    Функция ловит нажатия инлайн кнопок для выбора валюты и ее записи в БД.
    После выбора валюты происходит вызов клавиатуры для выбора интересующего курса.

    :param call:
    :return:
    """
    stripe = '-' * 50

    if call.data == 'usd_button':
        bot.send_message(call.message.chat.id, f'{stripe}\nВыбрана валюта: USD в руб\n{stripe}')
        write_currency_in_db(call.from_user.id, 'RUB=X')

    elif call.data == 'eur_button':
        bot.send_message(call.message.chat.id, f'{stripe}\nВыбрана валюта: EUR в руб\n{stripe}')
        write_currency_in_db(call.from_user.id, 'EURRUB=X')

    elif call.data == 'btc_usd_button':
        bot.send_message(call.message.chat.id, f'{stripe}\nВыбрана валюта: BTC в usd\n{stripe}')
        write_currency_in_db(call.from_user.id, 'BTC-USD')

    elif call.data == 'gold_button':
        bot.send_message(call.message.chat.id, f'{stripe}\nВыбрано: Золото в руб/г\n{stripe}')
        write_currency_in_db(call.from_user.id, 'GC=F, RUB=X')

    elif call.data == 'index500_button':
        bot.send_message(call.message.chat.id, f'{stripe}\nВыбран: S&P 500 в usd\n{stripe}')
        write_currency_in_db(call.from_user.id, '^GSPC')

    elif call.data == 'yuan_button':
        bot.send_message(call.message.chat.id, f'{stripe}\nВыбрана валюта: Юань в руб\n{stripe}')
        write_currency_in_db(call.from_user.id, 'CNYRUB=X')

    elif call.data == 'yen_button':
        bot.send_message(call.message.chat.id, f'{stripe}\nВыбрана валюта: Йена в руб\n{stripe}')
        write_currency_in_db(call.from_user.id, 'JPYRUB=X')

    bot.send_message(call.message.chat.id, 'Какой курс вас интересует:',
                     reply_markup=action_choice_keyboard())


@bot.callback_query_handler(func=lambda call: call.data == 'other_button')
def callback_currency_choice(call: CallbackQuery) -> None:
    """
    Функция ловит нажатие инлайн кнопки для ввода кода валюты вручную.
    Для этого устанавливается состояние input_currency и выводится сообщение пользователю с инструкцией.

    :param call:
    :return:
    """
    bot.set_state(call.from_user.id, MyStates.input_currency, call.message.chat.id)
    bot.send_message(call.message.chat.id, 'Введите символьный код необходимой валюты (если знаете),\n'
                                           'либо воспользуйтесь /list для просмотра доступных кодов')
