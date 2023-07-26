import os
import telebot
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(token)

if __name__ == '__main__':
    bot.polling()
