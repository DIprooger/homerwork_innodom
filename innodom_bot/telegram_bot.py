import telebot
import re
from telebot import types

TOKEN = '6935628256:AAG7WDhCF42l_zEDt4u173ovb3-ECk3qoTc'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(n):
    bot.send_message(n.chat.id, 'Привет, {0.first_name}! Введи математическое выражение: '.format(n.from_user))


@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        expression = message.text
        expression = re.sub(r'[^\d\+\-\*\/\(\)\.\,]', '', expression)

        result = eval(expression)

        bot.reply_to(message, f"Результат: {result}")
    except Exception as e:
        bot.reply_to(message, "Произошла ошибка при вычислении. Убедитесь, что введено корректное математическое "
                              "выражение.")


bot.polling()
