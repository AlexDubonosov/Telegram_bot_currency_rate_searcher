from loader import bot
from keyboards.inline import action_choice
from units.api import chosen_currency_price
from handlers.custom.change_date_state import change_date_state
from database.db_with_orm import write_data_in_db


@bot.callback_query_handler(func=lambda call:
                            call.data == 'current_button' or
                            call.data == 'low_button' or
                            call.data == 'high_button' or
                            call.data == 'custom_button')
def callback_action_choice(call):
    if call.data == 'current_button':
        result = chosen_currency_price('regularMarketPrice', call.from_user.id, 'regularMarketChange')
        if isinstance(result, tuple):
            if result[1] > 0:
                bot.send_message(call.message.chat.id, f'Текущая стоимость:  {result[0]} +{round(result[1], 3)}')
            else:
                bot.send_message(call.message.chat.id, f'Текущая стоимость:  {result[0]} {round(result[1], 3)}')
        else:
            bot.send_message(call.message.chat.id, f'Текущая стоимость:  {result}')

    elif call.data == 'low_button':
        result = chosen_currency_price('regularMarketDayLow', call.from_user.id)
        bot.send_message(call.message.chat.id, f'Минимальная цена за день:  {result}')

    elif call.data == 'high_button':
        result = chosen_currency_price('regularMarketDayHigh', call.from_user.id)
        bot.send_message(call.message.chat.id, f'Максимальная цена за день:  {result}')

    elif call.data == 'custom_button':
        change_date_state(call.message)


user_storage = {}


@bot.callback_query_handler(func=lambda call:
                            call.data == 'usd_button' or
                            call.data == 'eur_button' or
                            call.data == 'btc_usd_button' or
                            call.data == 'gold_button' or
                            call.data == 'sber_usd_button' or
                            call.data == 'index500_button' or
                            call.data == 'yuan_button' or
                            call.data == 'yen_button' or
                            call.data == 'other_button')
def callback_currency_choice(call):
    if call.data == 'usd_button':
        bot.send_message(call.message.chat.id, 'Выбрана валюта: USD в руб')
        write_data_in_db(user_storage, call.from_user.id, 'RUB=X')

    elif call.data == 'eur_button':
        bot.send_message(call.message.chat.id, 'Выбрана валюта: EUR в руб')
        write_data_in_db(user_storage, call.from_user.id, 'EURRUB=X')

    elif call.data == 'btc_usd_button':
        bot.send_message(call.message.chat.id, 'Выбрана валюта: BTC в usd')
        write_data_in_db(user_storage, call.from_user.id, 'BTC-USD')

    elif call.data == 'gold_button':
        bot.send_message(call.message.chat.id, 'Выбрано: Золото в руб/г')
        write_data_in_db(user_storage, call.from_user.id, 'GC=F, RUB=X')

    elif call.data == 'index500_button':
        bot.send_message(call.message.chat.id, 'Выбран: S&P 500 в usd')
        write_data_in_db(user_storage, call.from_user.id, '^GSPC')

    elif call.data == 'yuan_button':
        bot.send_message(call.message.chat.id, 'Выбрана валюта: Юань в руб')
        write_data_in_db(user_storage, call.from_user.id, 'CNYRUB=X')

    elif call.data == 'yen_button':
        bot.send_message(call.message.chat.id, 'Выбрана валюта: Йена в руб')
        write_data_in_db(user_storage, call.from_user.id, 'JPYRUB=X')

    elif call.data == 'other_button':
        bot.send_message(call.message.chat.id, 'Введите символьный код необходимой валюты,\n'
                                               'либо воспользуйтесь /list для просмотра доступных кодов')

    bot.send_message(call.message.chat.id, 'Какой курс вас интересует:',
                     reply_markup=action_choice.action_choice_keyboard())
