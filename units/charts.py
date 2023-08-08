import matplotlib.pyplot as plt
import matplotlib
import datetime
from units.twelve_date_from_list import twelve_date_from_list

# Исправляет ошибку UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail
matplotlib.use('agg')

# Описание для подготовленных валют
currency = {
    'RUB=X': 'Доллар',
    'EURRUB=X': 'Евро',
    'BTC-USD': 'Биткоин',
    'GC=F, RUB=X': 'Золото',
    '^GSPC': 'Акции 500 крупнейших компаний США',
    'CNYRUB=X': 'Юань',
    'JPYRUB=X': 'Йена'
}


# Сохраняет график картинкой
def get_charts(data: list, time_period: list, user_currency: list) -> None:

    # Повторяющиеся значения в ответе от api записываются как None, исправляем это, берем предыдущее значение.
    correct_data = []
    for index, value in enumerate(data):
        if value is None:
            value = data[index - 1]
            correct_data.append(value)
        else:
            correct_data.append(value)
    # размер графика
    plt.rcParams['figure.figsize'] = [10, 6]
    # строим график
    plt.plot([correct_data[key] for key in range(len(correct_data))], color='green')
    # подписи графика и осей
    plt.title(f"Стоимость валюты: {currency[user_currency[0]]}", fontsize=20)
    plt.ylabel('Стоимость')
    plt.xlabel('Выбранный диапазон дат')
    # значения оси X:
    # значений может быть от единиц до нескольких тысяч, сокращаем до +- 12, чтобы на графике это смотрелось органично
    short_time_period = twelve_date_from_list(time_period)
    short_time_period = [str(datetime.datetime.fromtimestamp(day)) for day in short_time_period]
    if len(time_period) > 12:
        shift = len(time_period) // 12
    else:
        shift = len(time_period)
    x_ticks = range(0, len(time_period), shift)
    plt.xticks(x_ticks, short_time_period, rotation=90)
    plt.tight_layout()
    # сохраняем полученный график
    plt.savefig('graf.png', dpi=300)
    # очистка текущего графического окна
    plt.clf()
