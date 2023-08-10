from loader import bot
from datetime import date
from telegram_bot_calendar import DetailedTelegramCalendar
from keyboards.reply.confirm_keyboard import confirm_keyboard
from states.user_state import MyStates
from database.db_with_orm import Currency


# Первый календарь для выбора стартовой даты
def my_calendar_start(message):
    calendar, step = DetailedTelegramCalendar(calendar_id=1, max_date=date.today()).build()
    return calendar


# Global переменная для записи дат
date_period = {}


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=1))
def cal(call):
    result, key, step = DetailedTelegramCalendar(calendar_id=1, max_date=date.today()).process(call.data)
    if not result and key:
        bot.edit_message_text(f"Начало периода:",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"Вы выбрали начала периода: {result}",
                              call.message.chat.id,
                              call.message.message_id)
        # Запись даты в global переменную с ключом from_user.id для уникальности юзеров
        date_period[call.from_user.id] = {"user": call.from_user.id}
        date_period[call.from_user.id]['user_date'] = []
        date_period[call.from_user.id]['user_date'].append(str(result))
        # Второй календарь для выбора конечной даты
        calendar, step = DetailedTelegramCalendar(calendar_id=2, max_date=date.today()).build()
        bot.send_message(call.message.chat.id, f"Конец периода:", reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=2))
def cal(call):
    result, key, step = DetailedTelegramCalendar(calendar_id=2, max_date=date.today()).process(call.data)
    if not result and key:
        bot.edit_message_text(f"Конец периода:",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"Вы выбрали конец периода {result}",
                              call.message.chat.id,
                              call.message.message_id)

        # Запись даты в global переменную с ключом from_user.id для уникальности юзеров
        # Запись получившихся дат в поле data_period в строку с самым большим id для конкретного юзера
        date_period[call.from_user.id]['user_date'].append(str(result))
        last_entry = Currency.select().where(Currency.user_id == call.from_user.id).order_by(Currency.id.desc()).first()
        last_entry.date_period = date_period[call.from_user.id]['user_date'][0] + " " + date_period[call.from_user.id]['user_date'][1]
        last_entry.save()

        # Клавиатура для подтверждения действия
        bot.set_state(call.from_user.id, MyStates.next_date, call.message.chat.id)
        bot.send_message(call.message.chat.id, 'Подтвердите ввод:', reply_markup=confirm_keyboard())

