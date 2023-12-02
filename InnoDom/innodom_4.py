# Задача 1
# Каждый 16 день от начала года Маша заказывает суши. Помогите посчитать, сколько дней в году Маша заказывает суши.
# Учтите, что в году не всегда 365 дней.


try:
    user_year = int(input("Enter yaer: "))
    print(e)
    if user_year % 4 == 0:
        print(f"An order of sushi a year {user_year}:", 366 // 16) 
    else:
        print(f"An order of sushi a year {user_year}:", 365 // 16)
except ValueError as e:
    print(e)
except NameError as e:
    print(e)
# Задача 2
# Есть список [98,67,92,112,68,39,98, 91,74,34,88]. Найдите среднее арифметическое этих значений.


list = [98,67,92,112,68,39,98, 91,74,34,88]
print(f"Arithmetic maen: {sum(list) / len(list):.5}")