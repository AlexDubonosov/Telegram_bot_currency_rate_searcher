from telebot.handler_backends import State, StatesGroup


# Класс для сменя состояний при опросе
class MyStates(StatesGroup):
    name = State()
    next_date = State()
