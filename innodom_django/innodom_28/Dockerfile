FROM ubuntu:20.04

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y python3 python3-pip nginx

# Установка зависимостей Python
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

# Копирование приложения в контейнер
COPY . /app/

# Копирование SQL-файла для инициализации базы данных
COPY /dump/innodom_27.sql /docker-entrypoint-initdb.d/

# Копирование конфигурационного файла nginx с кэшем и установкой таймаута
COPY nginx.conf /etc/nginx/sites-available/default

# Команда для запуска приложения
CMD ["sh", "-c", "python3 manage.py makemigrations && python manage.py