# Необходимо выполнить операцию вставки данных в несколько таблиц базы данных и убедиться, что эти операции выполняются
# все или ни одна. Используйте транзакцию, чтобы обеспечить атомарность операций. Если хотя бы одна из операций не
# выполнится успешно, все изменения должны быть отменены.


import psycopg2
import environ
import os


BASE_DIR = '/home/diana/Desktop/Python/тренировка/homerwor_programing_innodom/innodom_databese_python'

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

connection = psycopg2.connect(
    dbname=env('DB_NAME_POS'),
    user=env('DB_USER_POS'),
    password=env('DB_PASSWORD_POS'),
    host=env('DB_HOST_POS'),
    port=env('DB_PORT_POS')
)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Authors(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deletion TIMESTAMP DEFAULT NULL
""")

try:
    cursor.execute("BEGIN")

    cursor.execute("")

except:
    

# Вам предоставлена база данных со множеством записей. Необходимо оптимизировать производительность запроса, который
# выполняет поиск записей по определенному столбцу. Создайте подходящий индекс для этого столбца, чтобы ускорить
# выполнение запроса и снизить нагрузку на базу данных.


# Необходимо выполнить операцию обновления данных в нескольких связанных таблицах базы данных. Также нужно убедиться,
# что данные остаются целостными и в случае сбоя можно выполнить откат изменений. Используйте транзакцию для группировки
# операций обновления и создайте необходимые индексы для улучшения производительности запросов.

cursor.close()
connection.close()