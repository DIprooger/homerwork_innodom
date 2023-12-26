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
    name VARCHAR(30),
    country VARCHAR(40),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deletion TIMESTAMP DEFAULT NULL
    );
""")

try:
    cursor.execute("BEGIN")
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
    connection.rollback()

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

try:
    cursor.execute("BEGIN")
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
    connection.rollback()

cursor.execute("END")

# Необходимо выполнить операцию вставки данных в несколько таблиц базы данных и убедиться, что эти операции выполняются
# все или ни одна. Используйте транзакцию, чтобы обеспечить атомарность операций. Если хотя бы одна из операций не
# выполнится успешно, все изменения должны быть отменены.

try:
    cursor.execute("BEGIN")

    cursor.execute("""
        INSERT INTO Authors(id, name, country, date_of_birth)
        VALUES 
            (10, 'Jane Austen', 'United Kingdom', '1775-12-07')
    """)

    cursor.execute("""
        INSERT INTO Books (id, title, author_id, year, price)
        VALUES
            (10, 'Pride and Prejudice', 10, 1813, 200.00)
    """)
    connection.commit()

except Exception as e:
    print(e)
    connection.rollback()

cursor.execute("END")

# пример для проверки атамарности
try:
    cursor.execute("BEGIN")

    cursor.execute("""
        INSERT INTO Authors(id, name, country, date_of_birth)
        VALUES 
            (11, 'Jane Austen', 'United Kingdom', '1775-12-07')
    """)

    cursor.execute("""
        INSERT INTO Books (id, title, author_id, year, price)
        VALUES
            (11, 'Pride and Prejudice', 'd', 1813, 200.00)
    """)
    connection.commit()

except Exception as e:
    print(e)
    connection.rollback()

cursor.execute("END")

# Вам предоставлена база данных со множеством записей. Необходимо оптимизировать производительность запроса, который
# выполняет поиск записей по определенному столбцу. Создайте подходящий индекс для этого столбца, чтобы ускорить
# выполнение запроса и снизить нагрузку на базу данных.

try:
    cursor.execute("CREATE INDEX name_idx ON authors (name);")
    cursor.execute("""
        SELECT *
        FROM authors 
        WHERE name = 'J.R.R. Tolkien';
    """)
    for row in cursor.fetchall():
        print(row)
except Exception as e:
    print(e)
    cursor.execute("DROP INDEX name_idx;")

# Необходимо выполнить операцию обновления данных в нескольких связанных таблицах базы данных. Также нужно убедиться,
# что данные остаются целостными и в случае сбоя можно выполнить откат изменений. Используйте транзакцию для группировки
# операций обновления и создайте необходимые индексы для улучшения производительности запросов.

try:
    cursor.execute("BEGIN")

    cursor.execute("""
        UPDATE authors
        SET date_of_birth = date_of_birth + 1
        WHERE name = 'J.R.R. Tolkien';
    """)

    cursor.execute("""
        UPDATE books
        SET author_id = (
            SELECT id
            FROM authors
            WHERE name = 'J.R.R. Tolkien'
        );
    """)
    connection.commit()

except Exception as e:
    print(e)
    connection.rollback()

try:
    cursor.execute("BEGIN")

    cursor.execute("CREATE INDEX author_id_idx ON books (title);")
    cursor.execute("""
            SELECT *
            FROM books 
            WHERE title = 'One Hundred Years of Solitude';
        """)
    for row in cursor.fetchall():
        print(row)
    connection.commit()

except Exception as e:
    print(e)
    connection.rollback()

cursor.close()
connection.close()