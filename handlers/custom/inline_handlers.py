from loader import bot
from keyboards.inline import action_choice
from database import write_read_db
from units.api import chosen_currency_price
from handlers.custom.change_date_state import change_date_state
from handlers.calendar.calendar import my_calendar_start

@bot.callback_query_handler(func=lambda call:
                            call.data == 'current_button' or
                            call.data == 'low_button' or
                            call.data == 'high_button' or
                            call.data == 'custom_button')
def callback_action_choice(call):
    if call.data == 'current_button':
        result = chosen_currency_price('regularMarketPrice', call.message.chat.id)
        bot.send_message(call.message.chat.id, f'Текущая стоимость:  {result}')

    elif call.data == 'low_button':
        result = chosen_currency_price('regularMarketDayLow', call.message.chat.id)
        bot.send_message(call.message.chat.id, f'Минимальная цена за день:  {result}')

    elif call.data == 'high_button':
        result = chosen_currency_price('regularMarketDayHigh', call.message.chat.id)
        bot.send_message(call.message.chat.id, f'Максимальная цена за день:  {result}')

    elif call.data == 'custom_button':
        change_date_state(call.message)
#         bot.set_state(call.message.from_user.id, DateStates.next_date, call.message.chat.id)
#         bot.send_message(call.message.chat.id, '1111', reply_markup=my_calendar_start(call.message))
#         # bot.register_next_step_handler(call.message, send_chart_if_date_is_ready)
#         print(call.message.from_user.first_name)
#         bot.send_message(call.message.chat.id, 'Hi, write me a name')
#
#
# @bot.message_handler(state=DateStates.next_date)
# def send_chart_if_date_is_ready(message):
#     bot.send_message(message.chat.id, 'Строю график...')
#     api.print_charts(message.chat.id)
#     with open('graf.png', 'rb') as image:
#         bot.send_photo(message.chat.id, image)
#     os.remove('graf.png')
#     clear_date(message.chat.id)
#     bot.delete_state(message.from_user.id, message.chat.id)


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
        write_read_db.write_currency('RUB=X', call.message.chat.id)
    elif call.data == 'eur_button':
        bot.send_message(call.message.chat.id, 'Выбрана валюта: EUR в руб')
        write_read_db.write_currency('EURRUB=X', call.message.chat.id)
    elif call.data == 'btc_usd_button':
        bot.send_message(call.message.chat.id, 'Выбрана валюта: BTC в usd')
        write_read_db.write_currency('BTC-USD', call.message.chat.id)
    elif call.data == 'gold_button':
        bot.send_message(call.message.chat.id, 'Выбрано: Золото в руб/г')
        write_read_db.write_currency('GC=F, RUB=X', call.message.chat.id)
    elif call.data == 'index500_button':
        bot.send_message(call.message.chat.id, 'Выбран: S&P 500 в usd')
        write_read_db.write_currency('^GSPC', call.message.chat.id)
    elif call.data == 'yuan_button':
        bot.send_message(call.message.chat.id, 'Выбрана валюта: Юань в руб')
        write_read_db.write_currency('CNYRUB=X', call.message.chat.id)
    elif call.data == 'yen_button':
        bot.send_message(call.message.chat.id, 'Выбрана валюта: Йена в руб')
        write_read_db.write_currency('JPYRUB=X', call.message.chat.id)

    elif call.data == 'other_button':
        bot.send_message(call.message.chat.id, 'Введите символьный код необходимой валюты,\n'
                                               'либо воспользуйтесь /list для просмотра доступных кодов')

    bot.send_message(call.message.chat.id, 'Какой курс вас интересует:',
                     reply_markup=action_choice.action_choice_keyboard())
