# 1) Написать функцию, которая возвращает замыкание для                           
# вычисления факториала.                      

# try:
#     number = int(input("Enter number: "))
# except ValueError as e:
#     print(e)
#
# def factorial(number):
#     count = 1
#     def count_factorial():
#         nonlocal count
#         for i in range(1, number + 1):
#             count *= i
#         return count
#     return count_factorial
#
# result = factorial(number)
# print(f"Factorial {number}! = {result()}")


# 2) Создать функцию для генерации случайных паролей                         
# с заданной длиной, используя замыкания.

# import string, random
#
# try:
#     len_pasword = int(input("Enter the password length: "))
# except ValueError as e:
#     print(e)
#
# def password(len_pasword):
#     symbol = string.ascii_letters + string.digits + string.punctuation
#     user_password = [random.choice(symbol) for _ in range(len_pasword)]
#     user_password = "".join(user_password)
#     return user_password
#
# print(f"Generated password length {len_pasword} :", password(len_pasword))


# 3) Написать декоратор на валидацию пароля. Этот декоратор должен                           
# применяться к функции, которая пароль запрашивает.                           
# Если всё хорошо - выводить сообщение о том, что пароль валиден,                           
# в противном случае вывести, что что-то не так. (или кто захочет -                                 
# вывести конкретное сообщение, что в пароле не так.)

# **Критерии безопасности включают следующее:**
# **Длина пароля должна быть не менее 8 символов и не более 20**
# **Пароль должен содержать как минимум одну заглавную и одну строчную букву.**
# **Пароль должен содержать как минимум одну цифру и один символ.**


# import re
#
# def password_verification(fun):
#     def wrapper():
#         pasword = fun()
#         is_alnum_reg = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)"
#         symbol_reg = r"[!@#$%^&*?_|<>{}]"
#         if re.findall(symbol_reg, pasword):
#             if re.match(is_alnum_reg, pasword):
#                 if len(pasword) >= 8:
#                     print("Password is valid.")
#                 elif len(pasword) > 20:
#                     print("Password isn't valid. The password is longer than 20 characters.")
#                 else:
#                     print("Password isn't valid. The password is shorter than 8 characters.")
#             else:
#                 print("Password isn't valid. There are no Latin uppercase or lowercase letters in the password.")
#         else:
#             print("Password isn't valid. the password does not contain special characters.")
#     return wrapper
#
# @password_verification
# def input_password():
#     user_password = input("Enter you password: ")
#     return user_password
#
# input_password()



# 4) Когда-то давно была задача на расчёт индекса массы-тела.                           
# Перепишите эту задачу с использованием замыканий.


# try:
#     user_grouwth = float(input("Enter your growth (m.cm): "))
#     user_weight = float(input("Enter your weight (kg): "))
# except ValueError as e:
#     print(f"You didn't  enter grouwth or/and weight, {e}")
#
# def imt(user_grouwth, user_weight):
#     result = ''
#     def return_imt():
#         nonlocal result
#         imt = user_weight/(user_grouwth ** 2)
#         if 18.5 <= imt <= 25:
#             result = 'Optimal weight'
#         elif imt > 25:
#             result = 'Overweght'
#         else:
#             result = 'Insufficient weight'
#         return result
#     return return_imt
#
# result = imt(user_grouwth, user_weight)
# print(result())


# 5) Напишите декоратор, который будет применяться к функции,                         
# выводить информацию типа: какая функция была вызвана, какие                           
# у неё были параметры, сколько раз она была вызвана.   

import inspect
from os import path
from functools import wraps
import json
import inspect


def decorator(fun):
    if path.exists("count_fun.json"):
        with open("count_fun.json") as count:
            count_data = json.load(count)
    else:
        count_data = {}

    @wraps(fun)
    def wrapper(number):
        name_fun = fun.__name__
        atributs = inspect.signature(fun)
        if name_fun in count_data:
            count_data[name_fun]['calls'] += 1
        else:
            count_data[name_fun] = {"calls": 1, "attributes": str(atributs)}

        reade = (f"Name fuction: {name_fun}\nNumber of calls: {count_data[name_fun]['calls']}\n"
                 f"Function atributes: {count_data[name_fun]['attributes']}")
        print(reade)

        with open("count_fun.json", "w") as count:
            json.dump(count_data, count, indent=4)

        result = fun(number)
        print(result)

    return wrapper

@decorator
def squaring_number(number):
    return number ** 2

@decorator
def kub_number(number):
    return number ** 3

kub_number(3)
kub_number(6)
squaring_number(4)
squaring_number(5)

# 6) Напишите декоратор, который замеряет время выполнения вашей
# функции. Если время выполнения в пределах двух секунд - выводите                          
# что всё хорошо. В противном случае сообщение о том, что функция                                  
# (её имя) работает слишком медленно, её необходимо оптимизировать.


# import time
#
# try:
#     number = int(input("Enter the number: "))
# except ValueError as e:
#     print(e)
#
# def time_decorator(times):
#     def decorator(fun):
#         def wrapper(number):
#             time_1 = time.time()
#             fun(number)
#             time_2 = time.time()
#             if time_2 - time_1 <= times:
#                 print("All ok")
#             else:
#                 print(f"Function {fun.__name__} runs slowly(")
#         return wrapper
#     return decorator
#
#
# @time_decorator(2)
# def squaring_number(number):
#     count = 0
#     for i in range(number):
#        count += i ** 100
#     return print(count)
#
# squaring_number(number)