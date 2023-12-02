# Задача 1
# Напишите декоратор, который принимает аргумент - время, и замораживает выполнение функции на это время.


import time
try:
    times = int(input("Enter the second for which to freeze the function: "))
    number = int(input("Enter the number: "))
except ValueError as e:
    print(e)

def frozen_time(times):
    def decorator(fun):
        def wraper(number):
            time.sleep(times)
            fun(number)
        return wraper
    return decorator

@frozen_time(times)
def hard_funtion(number):
    return print(f"Execution of a function: {number**2}")   

hard_funtion(number)


# Задача 2
# Напишите функцию-генератор, генерирующий следующее чётное число.


def even_numbers(number):
    while True:
        if number % 2 == 0:
            yield number
            number += 2
        else:
            number += 1
            yield number
            number += 2

try:
    number = int(input("Enter the number: "))
except ValueError as e:
    print(e)

generator_numbers = even_numbers(number)
print(next(generator_numbers))
print(next(generator_numbers))
print(next(generator_numbers))
print(next(generator_numbers))
print(next(generator_numbers))


# Задача 3
# Напишите калькулятор на операции (+, -, *, /) с помощью lambda-функций.


number_1 = int(input("Enter the first number: "))
action = input("Enter action(+, -, *, /): ")
number_2 = int(input("Enter the first number: "))
#вариант 1
match action:
    case "+":
        result = lambda number_1, number_2: number_1 + number_2
        print(f"{number_1} + {number_2} = {result(number_1, number_2)}")
    case "-":
        result = lambda number_1, number_2: number_1 - number_2
        print(f"{number_1} - {number_2} = {result(number_1, number_2)}")
    case "*":
        result = lambda number_1, number_2: number_1 * number_2
        print(f"{number_1} * {number_2} = {result(number_1, number_2)}")
    case "/":
        result = lambda number_1, number_2: number_1 / number_2
        print(f"{number_1} / {number_2} = {result(number_1, number_2)}")

#вариант 2
def calculator(number_1, number_2, action):
    actions = {
        "+": lambda number_1, number_2: number_1 + number_2,
        "-": lambda number_1, number_2: number_1 - number_2,
        "*": lambda number_1, number_2: number_1 * number_2,
        "/": lambda number_1, number_2: number_1 / number_2,
    }
    result = actions[action]
    return print(f"{number_1} {action} {number_2} = {result(number_1, number_2)}")

calculator(number_1, number_2, action)