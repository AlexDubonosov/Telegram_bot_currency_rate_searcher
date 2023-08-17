"""
Модуль предназначен для хранения структуры БД
"""

from peewee import (
    CharField,
    ForeignKeyField,
    Model,
    SqliteDatabase,
)

from config_data.config import DATABASE_PATH

db = SqliteDatabase(DATABASE_PATH)


class BaseModel(Model):
    """
    Базовый класс для наследования, чтобы у всех моделей была единая БД
    """
    class Meta:
        """
        Ссылка на БД
        """
        database = db


class User(BaseModel):
    """
    Класс Пользователь, содержит необходимую информацию для идентификации:
    user_id - уникальный идентификатор
    user_first_name - ник в чате ТГ
    """
    user_id = CharField(primary_key=True)
    user_first_name = CharField()


class Currency(BaseModel):
    """
    Класс Валюта, содержит информацию о запрошенных валютах:
    user - ссылка на пользователя, выполняющего действие
    currency - название валюты
    date_period - необязательное поле содержащее даты начала и конца периода для построения графика
    """
    user = ForeignKeyField(User, backref='history')
    currency = CharField()
    date_period = CharField(null=True)


def create_models() -> None:
    """
    Функция для создания БД

    :return: - None
    """
    db.create_tables(BaseModel.__subclasses__())
