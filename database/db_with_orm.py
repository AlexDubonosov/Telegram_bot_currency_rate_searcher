import os
from peewee import (
    CharField,
    ForeignKeyField,
    Model,
    SqliteDatabase,
)


db = SqliteDatabase(os.path.abspath(os.path.join('database', 'bot.db')))


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = CharField(primary_key=True)
    user_first_name = CharField()


class Currency(BaseModel):
    user = ForeignKeyField(User)
    currency = CharField()
    date_period = CharField(null=True)


def create_models():
    db.create_tables(BaseModel.__subclasses__())


def write_data_in_db(storage, call, currency, date_period=None):
        storage[call] = {"user": call}
        storage[call]["currency"] = currency
        if date_period is not None:
            storage[call]["date_period"] = date_period
        Currency(**storage[call]).save()

