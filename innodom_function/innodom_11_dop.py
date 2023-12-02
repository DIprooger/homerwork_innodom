# Напишите функции:
# функция, которая принимает диапазон, генерирует и возвращает случайное целочисленное число


import random

# def number_random(numbers):
#     x, y = numbers
#     return random.randint(x, y)

# numbers = input("Enter 2 numbers with the spase: ").split()
# numbers = [int(i) for i in numbers]
# print(number_random(numbers))

# функция, которая принимает диапазон, генерирует и возвращает случайное вещественное число


def number_random(numbers):
    x, y = numbers
    return random.uniform(x, y)

numbers = input("Enter 2 numbers with the spase: ").split()
numbers = [int(i) for i in numbers]
print(number_random(numbers))


# функция, которая генерирует и возвращает случайное число


def number_random():
    return random.random()
print("Random number: ", number_random())


# функция, которая принимает список и возвращает перемешанный список


def number_random(symbols):
    random.shuffle(symbols)
    return symbols
symbols = input("Enter symbols with the spase: ").split()
print(number_random(symbols))


# функция, которая принимает список и возвращает случайный элемент из последовательности


def symbols_random(symbols):
    return random.choice(symbols)
symbols = input("Enter symbols with the spase: ").split()
print(symbols_random(symbols))