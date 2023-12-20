# В вашей базе данных есть таблица "Books" со следующими столбцами: "id" (целое число, первичный ключ), "title"
# (текстовый тип), "author" (текстовый тип), "year" (целое число) и "price" (вещественный тип). Вам необходимо
# выполнить следующие действия:


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
    CREATE TABLE IF NOT EXISTS Books(
        id INT PRIMARY KEY,
        title VARCHAR(50),
        author VARCHAR(30),
        year INT,
        price INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deletion TIMESTAMP DEFAULT NULL
    )
""")


# - вставьте несколько записей в таблицу "Books" с информацией о различных книгах, включая название, автора,
# год издания и цену.

cursor.execute("""
    INSERT INTO Books (id, title, author, year, price, created_at, deletion)
    VALUES
        (1, 'Роман любви', 'Лев Толстой', 1900, 150.00, CURRENT_TIMESTAMP, NULL),
        (2, 'Детективная история', 'Федор Достоевский', 1910, 200.00, CURRENT_TIMESTAMP, NULL),
        (3, 'Фантастическая технология', 'Дмитрий Быков', 2023, 999.99, CURRENT_TIMESTAMP, NULL),
        (4, 'Любовный роман', 'Александр Пушкин', 1820, 300.00, CURRENT_TIMESTAMP, NULL),
        (5, 'Приключенческий детектив', 'Иван Иванов', 2022, 400.00, CURRENT_TIMESTAMP, NULL),
        (6, 'Историческая фантастика', 'Петр Петров', 2021, 500.00, CURRENT_TIMESTAMP, NULL),
        (7, 'Технологический нон-фикшн', 'Сидоров Сидоров', 2020, 600.00, CURRENT_TIMESTAMP, NULL),
        (8, 'Любовная история', 'Лев Толстой', 1901, 700.00, CURRENT_TIMESTAMP, NULL),
        (9, 'Детективная история', 'Федор Достоевский', 1911, 800.00, CURRENT_TIMESTAMP, NULL),
        (10, 'Фантастическая технология', 'Дмитрий Быков', 2024, 900.00, CURRENT_TIMESTAMP, NULL);
    """)

print("_________________________________________________________________________________________________________________")
# - выберите все записи из таблицы "Books", отсортированные по году издания в порядке возрастания.

cursor.execute("""
    SELECT * FROM Books
    ORDER BY year      
""")
for row in cursor.fetchall():
    print(row)


print("_________________________________________________________________________________________________________________")
# - выберите книги, у которых цена выше определенного значения.

cursor.execute("""
    SELECT * FROM Books
    WHERE price > 400.00
""")

for row in cursor.fetchall():
    print(row)


print("_________________________________________________________________________________________________________________")
# - обновите цену книги с определенным ID.

cursor.execute("""
    UPDATE Books
    SET title = 'Новый роман любви'
    WHERE id = 1;
""")
cursor.execute("SELECT * FROM Books")
for row in cursor.fetchall():
    print(row)


print("_________________________________________________________________________________________________________________")
# - удалите книги, у которых год издания меньше определенного значения

cursor.execute("""
    UPDATE Books
    SET deletion = CURRENT_TIMESTAMP
    WHERE year < 2001;
""")
cursor.execute("""
    SELECT * FROM Books
    WHERE deletion IS NULL
""")

for row in cursor.fetchall():
    print(row)


cursor.close()
connection.close()