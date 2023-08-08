from loader import bot
from datetime import date
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from database.write_read_db import write_date, clear_date
from keyboards.reply.confirm_keyboard import confirm_keyboard
import handlers
from states.user_state import MyStates


# Первый календарь для выбора стартовой даты
def my_calendar_start(message):
    clear_date(message.chat.id)     # Очищаем все что могло быть в файле
    calendar, step = DetailedTelegramCalendar(calendar_id=1, max_date=date.today()).build()
    return calendar


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
        write_date(str(result), call.message.chat.id)    # Запись даты в файл
        # Второй календарь для выбора конечной даты
        calendar, step = DetailedTelegramCalendar(calendar_id=2, max_date=date.today()).build()
        bot.send_message(call.message.chat.id,
                         f"Конец периода:",
                         reply_markup=calendar
                         )


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
        write_date(str(result), call.message.chat.id)    # Запись даты в файл
        # Клавиатура для подтверждения действия
        bot.set_state(call.from_user.id, MyStates.next_date, call.message.chat.id)
        bot.send_message(call.message.chat.id, 'Подтвердите ввод:', reply_markup=confirm_keyboard())

