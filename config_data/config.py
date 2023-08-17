
"""
Модуль для хранения переменных
"""

import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены, т.к. отсутствует файл .env')
else:
    load_dotenv()


BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / 'database' / 'bot.db'

MENU_COMMANDS = (
    ("/start", "Запустить бота"),
    ('/currency', 'Выбрать валюту'),
    ('/history', 'Последние 10 запросов'),
    ("/help", "Вывести справку")
)

currency_description = {
    'RUB=X': 'Доллар',
    'EURRUB=X': 'Евро',
    'BTC-USD': 'Биткоин',
    'GC=F, RUB=X': 'Золото',
    '^GSPC': 'Акции 500 крупнейших компаний США',
    'CNYRUB=X': 'Юань',
    'JPYRUB=X': 'Йена'
}
