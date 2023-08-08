import matplotlib.pyplot as plt
import matplotlib
import datetime


# Исправляет ошибку UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail
matplotlib.use('agg')

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
def get_charts(
        data: list,
        time_period: list,
        user_currency: list
) -> None:

    correct_data = []
    for index, value in enumerate(data):
        if value is None:
            value = data[index - 1]
            correct_data.append(value)
        else:
            correct_data.append(value)

    plt.rcParams['figure.figsize'] = [10, 6]
    plt.plot([correct_data[key] for key in range(len(correct_data))], color='green')

    plt.title(f"Стоимость валюты: {currency[user_currency[0]]}", fontsize=20)
    plt.ylabel('Стоимость')
    plt.xlabel('Выбранный диапазон дат')
    short_time_period = [datetime.datetime.fromtimestamp(time_period[count]) for count in range(0, len(time_period), 12)]
    x_ticks = range(0, len(time_period), 12)
    plt.xticks(x_ticks, short_time_period, rotation=90)
    plt.tight_layout()

    plt.savefig('graf.png', dpi=300)
    plt.clf()
