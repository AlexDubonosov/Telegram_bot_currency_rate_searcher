"""
Модуль для загрузки переменных и создания Storage для хранения состояний пользователя
"""


import logging

import telebot
from telebot import TeleBot
from telebot.storage import StateMemoryStorage

from config_data import config

state_storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=state_storage)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

