from database.write_read_db import read_date
import datetime
import calendar


# Конвертирование дат из формата г/м/д в секунды с 'начала эпохи'
# Выбор интервала для графика в зависимости от промежутка
def convert_date(chat_id: str) -> tuple:
    date = read_date(chat_id)['date']

    y, m, d = date[0].split('-')
    st = datetime.datetime(int(y), int(m), int(d))
    start_time = str(calendar.timegm(st.timetuple()))

    y, m, d = date[1].split('-')
    et = datetime.datetime(int(y), int(m), int(d))
    end_time = str(calendar.timegm(et.timetuple()))

    if int(start_time) - int(end_time) > 604_800:
        interval = "1d"
    else:
        interval = '60m'

    return interval, start_time, end_time
