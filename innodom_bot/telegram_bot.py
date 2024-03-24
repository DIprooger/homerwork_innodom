import telebot
import re
import environ
import os
import psycopg2
from pathlib import Path

BASE_DIR = '/home/diana/Desktop/Python/тренировка/homerwor_programing_innodom/innodom_bot'

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

connection = psycopg2.connect(
    dbname=env('DB_NAME_POS'),
    user=env('DB_USER_POS'),
    password=env('DB_PASSWORD_POS'),
    host=env('DB_HOST_POS'),
    port=env('DB_PORT_POS')
)

TOKEN = env('TOKEN')
bot = telebot.TeleBot(TOKEN)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Bot(
    id SERIAL PRIMARY KEY,
    name VARCHAR(225),
    query_text VARCHAR(225),
    response_text VARCHAR(225),
    query_time TIMESTAMP DEFAULT NOW()
    );
""")
connection.commit()


def insert_query_into_database(name, query_text, response_text):
    try:
        cursor.execute(f"""
                INSERT INTO Bot(name, query_text, response_text)
                VALUES
                    (%s, %s, %s);
            """, (name, query_text, response_text))
        connection.commit()

    except Exception as e:
        print(e)


@bot.message_handler(commands=['start'])
def start(n):
    bot.send_message(n.chat.id, 'Привет, {0.first_name}! Введи математическое выражение: '.format(n.from_user))


@bot.message_handler(func=lambda message: True)
def calculate(message):
    user_name = message.from_user.username
    expression_text = message.text
    try:
        expression = re.sub(r'[^\d\+\-\*\/\(\)\.\,]', '', expression_text)
        result = eval(expression)
        bot.reply_to(message, f"Результат: {result}")
        insert_query_into_database(user_name, expression, result)

    except Exception as e:
        result = "Произошла ошибка при вычислении. Убедитесь, что введено корректное математическое выражение."
        bot.reply_to(message, result)
        insert_query_into_database(user_name, expression_text, 'Ошибка')



bot.polling()
cursor.close()
connection.close()
