# Переписать задачи работы с файлами с наших домашек, на классы.

# Есть файл titanic.txt.Нужно открыть его и вывести содержимое.
# Из уже существующего файла titanic.txt посчитайте количество строк и выведите их.
# Откройте существующий файл titanic.txt, запишите последние две
#  строки из этого файла в новый файл some_info_about_titanic.txt


import os
class Titanic:
    with open("titanic.txt", "r", encoding="utf-8") as titanic:
        titanic_readline = titanic.readlines()
    with open("titanic.txt", "r", encoding="utf-8") as titanic:
        titanic_read = titanic.read()

    def __init__(self):
        self.titanic_readline
        self.titanic_read

    def __str__(self):
        return str(self.titanic_read)

    def __len__(self):
        return len(self.titanic_readline)

    def wriete_two_last_line(self):
        with open("some_info_about_titanic.txt", "w", encoding="utf-8") as some_titanic:
            for element in self.titanic_readline[-2:]:
                some_titanic.write(element)
        if os.path.exists("some_info_about_titanic.txt"):
            return "Filee with name 'some_info_about_titanic.txt' create"
        else:
            return "Filee with name 'some_info_about_titanic.txt' not create"

titanic = Titanic()
print(titanic)
print("Line in this text:", len(titanic))
print(titanic.wriete_two_last_line())


# Пользователь вводит разные данные с клавиатуры. Если он вводит
# строку - записать её в файл user_response.txt. Если вводит число - пропускать его.

class UserText:
    def __init__(self, user_text):
        self.user_text = user_text

    def user_text_wreite(self):
        with open("user_response.txt", "a") as user_respons:
            if not (user_text.isdigit()):
                print("Your text is writing in fille")
                user_respons.write(user_text + '\n')
            else:
                print("Your text is number")


user_text = input("Enter your tetx: ")
wriete = UserText(user_text)
wriete.user_text_wreite()


# Считайте лог-файл 'requests.log', а затем проанализируйте его, выводя количество
# запросов по каждому IP-адресу.

class Reguest:
    ip = set()
    ip_dictionary = {}

    def __init__(self):
        self.ip
        self.ip_dictionary

    def readline_request(self):
        with open("requests.log", "r") as requests:
            requests_lines = requests.readlines()
            for element in requests_lines:
                element_list = element.split(" ")
                self.ip.add(element_list[0])

    def write_count_ip(self):
        with open("requests.log", "r") as requests:
            for_count = requests.read()
            for key in self.ip:
                self.ip_dictionary[key] = for_count.count(key)
        return self.ip_dictionary


reques = Reguest()
reques.readline_request()
print(reques.write_count_ip())

# Есть файл log.txt. Откройте его, найдите только строки, в которых
# выведены ошибки. Эти строки запишите в отдельный файл errors.txt


class Erros:

    with open("requests.log", "r") as requests, open("errors.txt", "w") as errors:
        list_requests = requests.readlines()
        for elemen in list_requests:
            if '404' in elemen:
                errors.write(elemen)

Erros()

# Реализовать небольшую систему входа:
# 1.вместо базы данных использовать csv файл
# пользователь может создать аккаунт (name, email, password, repeat_password)
# 2.Реализовать создание аккаунта. проверить наличие такого пользователя
# по email. Если есть - вывести сообщение, что такой пользователь
# уже есть, аккаунт создать нельзя. Если нет - создать аккаунт,
# данные записать в csv файл.
# 3.Реализация входа в систему. Проверять наличие пользователя по email.
# 4.Проверка пароля. Учесть все возможные расхождения, ошибки.
# 5.Все данные берутся и записываются из csv файла.
# 6.Пароль должен валидироваться. Можете написать его реализацию через staticmethod

import csv
import os
import re


# with open("users.csv", "w") as user:
#     field_name = ["name", "email", "password", "repeat password"]
#
#     writer = csv.DictWriter(user, fieldnames=field_name)
#     writer.writeheader()
#
#     writer.writerow({"name": "Diana", "email": "dfprivet@gmail.com", "password": "Dd$485720vnjdv", "repeat_password": "Dd$485720vnjdv"})
#     writer.writerow({"name": "Pacha", "email": "pacha@gmail.com", "password": "Dd$485720pach", "repeat_password": "Dd$485720pach"})
#     writer.writerow({"name": "Meg", "email": "meg@gmail.com", "password": "Mm#$334dfe", "repeat_password": "Mm#$334dfe"})

class Entry:
    user_authorization = {}
    user_email = ''

    def __init__(self):
        if os.path.exists("users.csv"):
            print("The file users.csv is ready for reading and writing.")
        else:
            with open("users.csv", "w") as user:
                field_name = ["name", "email", "password", "repeat password"]

                writer = csv.DictWriter(user, fieldnames=field_name)
                writer.writeheader()
            print("The file users.csv is ready for reading and writing.")

    def email(self, email):
        with open("users.csv", "r") as user:
            read = csv.DictReader(user)
            for element in read:
                if element["email"] == email:
                    print(f"Welcome {element['name']}")
                    return False
                else:
                    print("You are not in the system. We begin authorization.")
                    self.user_email = email
                    return True

    def name(self, name):
        if name.isalpha():
            self.user_authorization["name"] = name
            self.user_authorization["email"] = self.user_email
            print(self.user_authorization)
            return False
        else:
            print("the name must contain only Latin letters!!!")
            return True

    def password(self, password):
        is_alnum_reg = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)"
        symbol_reg = r"[!@#$%^&*?_|<>{}]"
        if len(password) >= 8:
            if re.match(is_alnum_reg, password):
                if re.findall(symbol_reg, password):
                    print("Password is valid.")
                    self.user_authorization["password"] = password
                    print(self.user_authorization)
                    return False
                else:
                    print("Password isn't valid. the password does not contain special characters.")
                    return True
            else:
                print("Password isn't valid. There are no Latin uppercase or lowercase letters in the password.")
                print("and/or there are no number")
                return True
        elif len(password) > 20:
            print("Password isn't valid. The password is longer than 20 characters.")
            return True
        else:
            print("Password isn't valid. The password is shorter than 8 characters.")
            return True

    def repeat_password(self, repeat):
        if self.user_authorization["password"] == repeat:
            print("The passwords matches.")
            self.user_authorization["repeat password"] = repeat
            print(self.user_authorization)
            return False
        else:
            print("The passwords did not match.")
            return True

    def write_users(self):
        with open("users.csv", "a") as user:
            field_name = ["name", "email", "password", "repeat password"]
            writer = csv.DictWriter(user, fieldnames=field_name)
            writer.writeheader()
            writer.writerow(self.user_authorization)
            print("User created")
            return False


print("Press 'q' to exit")
command = ''
flag = True
flag_user = True

while command != "q" and flag:
    user = Entry()
    command = input("Enter your email: ")

    if command == 'q':
        break
    flag = user.email(command)

    if flag:
        while flag_user:
            command = input("Enter your name: ")
            if command == 'q':
                break
            flag_user = user.name(command)
        flag_user = True

        if command == 'q':
            break

        while flag_user:
            command = input("Enter password: ")
            if command == 'q':
                break
            flag_user = user.password(command)
        flag_user = True

        if command == 'q':
            break

        while flag_user:
            command = input("Please repeat your password.: ")
            if command == 'q':
                break
            flag_user = user.repeat_password(command)
        flag_user = True

        if command == 'q':
            break
        flag = user.write_users()
