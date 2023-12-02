# Задача 1
# Пользователь вводит список с глубиной 2. Количество столбцов совпадает с количеством срок. Поменяйте 
# столбцы и строки местами.
# Вход:
# [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]
# Выход:
# [[1,4,7],
# [2,5,8],
# [3,6,9]]


# matrix = []
# count = 1
# try:
#     dimension = int(input("Dimension of matrix: "))
# except ValueError as e:
#     print(e)

# while count <= dimension**2:
#     element = []
#     for i in range(dimension):
#         element.append(count)
#         count += 1
#     matrix.append(element)

# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         print(matrix[j][i], end = ', ')
#     print()

# Задача 2
# Напишите функцию для вычисления факториала числа рекурсивно и итеративно. Факториал числа – 
# это произведение от 1 до числа (10! = 1*2*3*4*5*6*7*8*9*10).

#вариант1
def factorial(number):
    if number == 1:
        return number
    else:
        return factorial(number-1) * number

try:
    number = int(input("Enter number: "))
except ValueError as e:
    print(e)

print(F"Factorial {number}: {factorial(number)}")

#вариант2
try:
    number = int(input("Enter number: "))
except ValueError as e:
    print(e)

def factorial_interator(number):
    while number >= 0:
        yield number
        number -= 1

result = 1
factorial_ = factorial_interator(number)
for i in range(number): result *= next(factorial_)

print(F"Factorial {number}: {result}")