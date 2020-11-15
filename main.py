import telebot
import os
from parser_p.parser import get_content
from relevance import entry_relevance, return_dic

import schedule
import time

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode=None)


string = '''Зравствуйте, вас приветствует служба поддержки Ростелекома.
Пожалуйста введите ваш запрос...'''


# shedule работа со временем(должен выполняться пока запущена прогга
schedule.every().monday.at('01:00').do(get_content)
schedule.run_pending()
time.sleep(1)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, string)


@bot.message_handler(content_types=['text'])
def send_answer(message):
	bot.send_message(message.chat.id, '''Ожидайте, ваш запрос обрабатывается...''')
	answer = entry_relevance(str(message))
	bot.send_message(message.chat.id, answer)
	bot.send_message(message.chat.id, '''Пожалуйста введите ваш запрос...''')


bot.polling()