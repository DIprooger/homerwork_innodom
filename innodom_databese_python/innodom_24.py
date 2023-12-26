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

# для дополнительного
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Authors(
    id INT PRIMARY KEY,
    name VARCHAR(30),
    country VARCHAR(40),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deletion TIMESTAMP DEFAULT NULL
    );
""")

try:
    connection.begin()
    cursor.execute("""
        INSERT INTO Authors(id, name, country, date_of_birth)
        VALUES
            (1, 'J.R.R. Tolkien', 'United Kingdom', '1892-01-31'),
            (2, 'Stephen King', 'United States', '1947-09-21'),
            (3, 'Paulo Coelho', 'Brazil', '1947-08-24'),
            (4, 'J.K. Rowling', 'United Kingdom', '1965-07-31'),
            (5, 'George R.R. Martin', 'United States', '1948-09-20'),
            (6, 'Gabriel García Márquez', 'Colombia', '1927-03-06'),
            (7, 'Harper Lee', 'United States', '1926-04-28'),
            (8, 'Agatha Christie', 'United Kingdom', '1890-09-15'),
            (9, 'Mark Twain', 'United States', '1835-11-30');
    """)
    connection.commit()
except Exception as e:
    print(e)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books(
        id INT PRIMARY KEY,
        title VARCHAR(50),
        author_id INT NOT NULL,
        year INT,
        price INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deletion TIMESTAMP DEFAULT NULL,
        FOREIGN KEY (author_id) REFERENCES Authors(id)
    )
""")

# - вставьте несколько записей в таблицу "Books" с информацией о различных книгах, включая название, автора,
# год издания и цену.

try:
    connection.begin()
    cursor.execute("""
        INSERT INTO Books (id, title, author_id, year, price)
        VALUES
            (1, 'The Lord of the Rings', 1, 1954, 150.00),
            (2, 'Carrie', 2, 1974, 300.00),
            (3, 'The Alchemist', 3, 1988, 999.99),
            (4, 'Harry Potter and the Philosopher`s Stone', 4, 1997, 300.00),
            (5, 'A Song of Ice and Fire', 5, 1996, 400.00),
            (6, 'One Hundred Years of Solitude', 6, 1967, 500.00),
            (7, 'To Kill a Mockingbird', 7, 1960, 600.00),
            (8, 'Murder on the Orient Express', 8, 1934, 700.00),
            (9, 'The Adventures of Tom Sawyer', 9, 1876, 800.00)
        """)
    connection.commit()
except Exception as e:
    print(e)


print("_________________________________________________________________________________________________________________")
# - выберите все записи из таблицы "Books", отсортированные по году издания в порядке возрастания.

cursor.execute("""
    SELECT * FROM Books
    ORDER BY year      
""")
for row in cursor.fetchall():
    print(row)

print(
    "_________________________________________________________________________________________________________________")
# - выберите книги, у которых цена выше определенного значения.

cursor.execute("""
    SELECT * FROM Books
    WHERE price > 400.00
""")

for row in cursor.fetchall():
    print(row)

print(
    "_________________________________________________________________________________________________________________")
# - обновите цену книги с определенным ID.

cursor.execute("""
    UPDATE Books
    SET title = 'Новый роман любви'
    WHERE id = 1;
""")
connection.commit()

cursor.execute("SELECT * FROM Books")
for row in cursor.fetchall():
    print(row)

print(
    "_________________________________________________________________________________________________________________")
# - удалите книги, у которых год издания меньше определенного значения

cursor.execute("""
    UPDATE Books
    SET deletion = CURRENT_TIMESTAMP
    WHERE year < 1950;
""")
connection.commit()

cursor.execute("""
    SELECT * FROM Books
    WHERE deletion IS NULL
""")

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
