# В вашей базе данных есть таблица "Books" со следующими столбцами: "id" (целое число, первичный ключ), "title"
# (текстовый тип), "author" (текстовый тип), "year" (целое число) и "price" (вещественный тип). Вам необходимо
# выполнить следующие действия:
# - вставьте несколько записей в таблицу "Books" с информацией о различных книгах, включая название, автора,
# год издания и цену.
# - выберите все записи из таблицы "Books", отсортированные по году издания в порядке возрастания.
# - выберите книги, у которых цена выше определенного значения.
# - обновите цену книги с определенным ID.
# - удалите книги, у которых год издания меньше определенного значения


import psycopg2
import environ
import os
from urllib.parse import quote

BASE_DIR = '/home/diana/Desktop/Python/тренировка/homerwor_programing_innodom/innodom_databese_python'

env = environ.Env(frame=None)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

connection = psycopg2.connect(
    dbname=env('DB_NAME_POS'),
    user=env('DB_USER_POS'),
    password=env('DB_PASSWORD_POS'),
    host=env('DB_HOST_POS'),
    port=env('DB_PORT_POS')
)

# connection.connect()
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books(
        id INT PRIMARY KEY,
        title VARCHAR(50),
        author VARCHAR(30),
        year INT,
        price INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT NULL       
    )
""")

connection.commit()
cursor.close()
connection.close()
