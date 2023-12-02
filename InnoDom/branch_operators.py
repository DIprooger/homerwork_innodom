# **or:**
# Задача 1. Создайте программу, которая проверяет, является ли число кратным 3 или 5.


try:
    number = float(input('Enter the number:'))
except ValueError as e:
    print(f"You did't enter a number, {e}!")
if number % 3 == 0 or number % 5 == 0:
    print('The nuber is a multiple 3 or 5')
else:
    print('The number is not a multiple 3 or 5')


# **Проверка пароля:**                           
# Задача 2. Напишите программу, которая запрашивает у пользователя                  
# пароль. Если пароль равен "secret", выведите "Доступ разрешен", в                   
# противном случае выведите "Доступ запрещен". 


try:
   user_password = input('Enter your password: ')
   if user_password == '':
       raise Exception("You have not entered your password!")
except Exception as e:
    print(e)
if user_password == 'secret':
    print('The password is correct')
else:
    print('The password is not correct')


# **Проверка числа на четность:**                               
# Задача 3. Попросите пользователя ввести целое число. Если число четное,                             
# выведите "Число четное", иначе выведите "Число нечетное".                             


try:
    user_number = int(input('Enter your an integer: '))
    if user_number % 2 == 0:
       print('The integer is even number')
    else:
        print('The integer is not an even number')
except (ValueError, NameError) as e:
    print(f"You did not enter an integer, {e}")


# **Калькулятор для двух чисел:**                                  
# Задача 4. Запросите у пользователя два числа и оператор (+, -, *, /). Выполните                                 
# соответствующее математическое действие и выведите результат.                            
# Обработайте случай деления на ноль.                   


try:
    number_1 = float(input("Plese enter the first number: "))
    number_2 = float(input("Plese enter the second number: "))
    mathematical_operation = input("Plese enter one of the following symbols (+, -, *, /): ")
    if mathematical_operation == '+':
        print(number_1, "+", number_2, "=", number_1 + number_2)
    elif mathematical_operation == '-':
        print(number_1, "-", number_2, "=", number_1 - number_2)
    elif mathematical_operation == '*':
        print(number_1, "*", number_2, "=", number_1 * number_2)
    elif mathematical_operation == '/':
        print(number_1, "/", number_2, "=", number_1 / number_2)
    else:
        raise Exception("You didn't enter one of the following symbols (+, -, *, /)")
except ValueError as e:
    print(f"You didn't a number, {e}")
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)


# **Проверка года на високосность:**                                
# Задача 5. Запросите у пользователя год. Проверьте, является ли этот год                               
# високосным, и выведите соответствующее сообщение.                             
# Год високосный, если он делится на 4, но не делится на 100,                                             
# за исключением случаев, когда он делится на 400 

try:
    user_year = int(input("Enter the year: "))
    if user_year % 4 == 0:
        print("It's a leap year")
    else:
        print("It's not a leap year")
except ValueError as e:
    print(e)


# **Расчет стоимости билета:**                            
# Задача 6. Попросите пользователя ввести возраст и тип билета ("детский",                             
# "взрослый", "пенсионер"). Рассчитайте стоимость билета с учетом                            
# скидок (50% скидка для детей и пенсионеров)

#       Зачем возраст, по типу билета можно посчитать стоимость.
#       Переделаю условие введите количество человек и тип каждого билета по очереди


print("One ticket coust 8 rubel.")
cost_ticket = 8
entire_cost = 0
try:
    number_clients = int(input("How many people: "))
    for i in range(number_clients):
        type_ticket = input("Write the type ot yopur ticket (child, adult, pension): ")
        if type_ticket == 'child' or type_ticket == 'pension':
            entire_cost += cost_ticket * .5
        elif type_ticket == 'adult':
            entire_cost += cost_ticket
        else:
            raise Exception("You didn't write the type ot yopur ticket (child, adult, pension)!")
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("You will pay:", entire_cost, "rubles")


# **Определение времени суток:**                              
# Задача 7. Попросите пользователя ввести текущее время (HH:MM).                                
# Выведите сообщение, соответствующее времени суток:                              
# "Утро", "День", "Вечер", "Ночь".


try:
    user_time = [int(i) for i in input("Enter the time (HH:MM): ").split(":")]
    if  6 <= user_time[0] < 12:
        print("Morning")
    elif 12 <= user_time[0] < 18:
        print("Day")
    elif 18<= user_time[0] < 24:
        print("Evening")
    elif 24 <= user_time[0] < 6:
        print("Night")
    else:
        raise Exception("You didn't enter the time (HH:MM):")
except ValueError as e:
    print(f"You didn't enter the time (HH:MM), {e}")        
except Exception as e:
    print(e)


# **Расчет налога на доход:**                              
#Задача 8. Введите годовой доход пользователя. Рассчитайте налог на                                      
# доход с учетом ставок: до $10,000 - 10%, от $10,000 до                                  
# $50,000 - 20%, свыше $50,000 - 30%.


try:
    user_income = float(input("Enter your income: "))
    taxes = 0
except ValueError as e:
    print(f"You didn't enter your income, {e}")
else:
    if user_income < 10000:
        taxes += user_income * .1
    elif 10000 <= user_income < 50000:
        taxes += user_income * .2
    elif 50000 <= user_income:
        taxes += user_income * .3
    print("You taxes:", taxes)
    print("You final income:", user_income - taxes)


# **Проверка на принадлежность к диапазону чисел:**                              
# Задача 9. Попросите пользователя ввести число. Проверьте, принадлежит ли                                  
# число диапазону от 10 до 20 включительно.                               


try:
    user_nuber = int(input("Enter your number: "))
except ValueError as e:
    print(f"You did't enter number, {e}")
else:
    if 10 <= user_nuber <= 20:
        print("Number betweeen 10 and 20")


# **Калькулятор BMI (Индекс массы тела):**                                 
# Задача 10. Запросите у пользователя его вес (кг) и рост (м). Рассчитайте                                  
# его BMI по формуле BMI = вес / (рост^2) и выведите сообщение,                             
# указывающее на его состояние: "Недостаточный вес",                               
# "Норма", "Избыточный вес", "Ожирение".


try:
    user_grouwth = float(input("Enter your growth (m.cm): "))
    user_weight = float(input("Enter your weight: "))
except ValueError as e:
    print(f"You didn't  enter grouwth or/and weight, {e}")
else:
    imt = user_weight/(user_grouwth ** 2)
    if 18.5 <= imt <= 25:
        print('Optimal weight')
    elif imt > 25:
        print('Overweght')
    else:
        print('Insufficient weight')


# **Конвертер температуры:**                                 
# Задача 11. Попросите пользователя ввести температуру в градусах Цельсия.                        
# Затем спросите, в какую шкалу он хочет конвертировать                                   
# (Фаренгейт или Кельвин). Выполните конвертацию и                                      
# выведите результат.                                  


try:
    user_celsius = int(input("Enter degred Celsius: "))
    fahrenheit_or_calvin = input("Enter Fahrenheigt(f) or Calvin(c): ").lower()
    if fahrenheit_or_calvin == 'Fahrenheigt' or fahrenheit_or_calvin == 'f':
        print("Fahrenheigt: ", user_celsius * 9 / 5 + 32)
    elif fahrenheit_or_calvin == 'Calvin' or fahrenheit_or_calvin == 'c':
        print("Calvin: ", user_celsius + 273.15)
    else:
        raise Exception("You didn't enter Fahrenheigt or Calvin!")
except ValueError as e:
    print(e)
except Exception as e:
    print(e)

# **Расчет кредита:**                                       
# Задача 12. Попросите пользователя ввести сумму кредита, процентную ставку и                                   
# срок кредита (в годах). Рассчитайте ежемесячный платеж и                                  
# общую сумму, которую придется заплатить. Обработайте                                     
# возможные ошибки ввода.                                     
# POV: спец формула для расчёта ежемесячного платежа:
# M = P[r(1+r)^n] / [(1+r)^n-1]

try:
    user_credit = float(input("Enter your credit: "))
    user_interest_rate = float(input("Enter your interest rate: ")) * .01 /12
    user_yare = float(input("Enter yare: ")) * 12
except ValueError as e:
    print(e)
else:
    mounth_pay = user_credit * user_interest_rate * (1 + user_interest_rate) ** (user_yare) / ((1 + user_interest_rate) ** (user_yare) - 1)
    print("Monthly payment:", mounth_pay)
    user_credit = (mounth_pay * user_yare)
    print("You need pay:", user_credit)
