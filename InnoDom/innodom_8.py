# Задача 1
# Пользователь вводит числа. Умножьте все чётные числа на 1.5, а нечётные - на 2.


numbers = input("Enter rhe numbers with a space: ").strip().split() 
try:
    numbers = [int(i) for i in numbers]
except ValueError as e:
    print(e)
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] *= 1.5
    else:
        numbers[i] *= 2
print(*numbers)


# Задача 2
# Есть ряд 1, 2, 4, 8, 16, 32, 64 … Посчитайте сумму n-элементов такого ряда.


# через сумму геометрической прогресии
try:
    n = int(input("Enter the numbers: "))
except ValueError as e:
    print(e)
a1 = 1
print("Smma:", a1*(2**n - 1))   

# #через цикл
numbers = [1]
for i in range(n-1):
    numbers.append(numbers[i]*2)
print(sum(numbers))


# Задача 3
# Пользователь вводит список строк и чисел. Если элемент является числом, 
# то выведите квадрат этого числа, если нет, то строку с элементами в обратном порядке.
# Проверка типа осуществляется с помощью type(num) == int. Результат функции приравнивается к типу 
# (int, float, list, str и другие).

# зачем писать type(num) == int, если все что мы вводим строка, если пытаемся переводчить то может попасть строка и дать ошибку????


user_enter = input("Enter somthing with a space in it: ").split()

for i in user_enter:
    try: 
        float(i)
    except ValueError:
        print(i[::-1], '-str')
    else:
        print(float(i)**2, '-float')