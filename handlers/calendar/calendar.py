"""
Модуль для отображения календаря для ввода дат начала и конца периода для построения графика курса валют
"""

from loader import bot
from datetime import date
from telegram_bot_calendar import DetailedTelegramCalendar
from keyboards.reply.confirm_keyboard import confirm_keyboard
from states.user_state import MyStates
from database.db_with_orm import write_date_period_in_db_in_last_slot_for_user
from units.check_date import check_date
from telebot.types import CallbackQuery


def my_calendar_start() -> DetailedTelegramCalendar:
    """
    Функция создает первый календарь для пользователя.

    :return:
    """
    calendar, step = DetailedTelegramCalendar(calendar_id=1, max_date=date.today()).build()
    return calendar


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=1))
def cal(call: CallbackQuery) -> None:
    """
    Функция вызывает первый календарь и дает выбрать дату начала периода.
    После записывает дату и хранилище и создает второй календарь для выбора даты конца периода.

    :param call:
    :return:
    """
    result, key, step = DetailedTelegramCalendar(calendar_id=1, max_date=date.today()).process(call.data)
    if not result and key:
        bot.edit_message_text("Начало периода:",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text("Вы выбрали начала периода: {result}",
                              call.message.chat.id,
                              call.message.message_id)

        # Устанавливаем состояние next_date
        bot. set_state(call.from_user.id, MyStates.next_date, call.message.chat.id)
        # Записываем дынные в ОП
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            data['date_period'] = []
            data['date_period'].append(str(result))

        # Создаем второй календарь для выбора конечной даты
        calendar, step = DetailedTelegramCalendar(calendar_id=2, max_date=date.today()).build()
        bot.send_message(call.message.chat.id, "Конец периода:", reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=2))
def cal(call: CallbackQuery) -> None:
    """
    Функция вызывает второй календарь и дает выбрать дату конца периода.
    Записывает дату в хранилище.
    Происходит проверка валидности дат.
    Если даты корректны - они записываются в БД, если нет вызывается предупреждение

    :param call:
    :return:
    """
    result, key, step = DetailedTelegramCalendar(calendar_id=2, max_date=date.today()).process(call.data)
    if not result and key:
        bot.edit_message_text("Конец периода:",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text("Вы выбрали конец периода {result}",
                              call.message.chat.id,
                              call.message.message_id)

        # Записываем данные в оперативную память
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            data['date_period'].append(str(result))

        # Проверка валидности полученных дат
        is_date = check_date(data['date_period'])

        if is_date:
            # Считываем ОП и записываем даты в БД
            with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
                write_date_period_in_db_in_last_slot_for_user(call.from_user.id, data)
            # bot.set_state(call.from_user.id, MyStates.next_date, call.message.chat.id)
            # Клавиатура для подтверждения действия
            bot.send_message(call.message.chat.id, 'Подтвердите ввод:', reply_markup=confirm_keyboard())
        else:
            bot.set_state(call.from_user.id, MyStates.not_state, call.message.chat.id)
            bot.send_message(call.message.chat.id, 'К сожалению я не могу обработать полученные даты...\n'
                                                   'Пожалуйста, учтите:\n'
                                                   '1. дата начала отсчета должна быть меньше даты конца отсчета.\n'
                                                   '2. Минимальный интервал 2 дня.\n\n'
                                                   'Введите /currency для продолжения, либо воспользуйтесь меню.\n')
