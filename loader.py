import telebot
from telebot import TeleBot
from config_data import config
from telebot.storage import StateMemoryStorage
import logging


state_storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=state_storage)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

