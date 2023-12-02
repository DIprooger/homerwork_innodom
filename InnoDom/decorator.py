# **Создание декоратора для измерения времени выполнения функции.**
# Напишите декоратор, который будет измерять время выполнения функции                              
# и выводить его на экран. Затем примените этот декоратор к любой                            
# функции, чтобы измерить ее время выполнения.    


from datetime import datetime 
from typing import Callable

def measure_time_decorator(fun: Callable):
   def wrapper(): 
       start_time = datetime.now()
       fun()
       end_time = datetime.now()
       execution_time = end_time - start_time
       print("Function execution time:", execution_time)
   return wrapper

@measure_time_decorator
def sguare_number():
    try:
        number = int(input("Enter you number: "))
    except ValueError as e:
        print(e)
    print(number**2)

sguare_number()


# **Создание декоратора для логирования.**
# Напишите декоратор, который будет записывать в файл логи информацию о                          
# вызовах функции, а именно ее имя и переданные аргументы. Затем                           
# примените этот декоратор к нескольким функциям и проверьте,                     
# что логи записываются правильно.                        


def logging_decorator(func):
    
    def wraper(*args, **kwarks):
        with open("file_name_function.txt", "a", encoding="utf-8") as file:
            result = func(*args, **kwarks)
            print(f"Name function {func.__name__}. positional arguments of function {args}. named fuction arguments {kwarks}/n", file=file)
        return result
    return wraper

@logging_decorator
def my_func(a, b, c, d):
    return a + b, c * d

my_func(2, 3, c=3, d=5)


# **Создание декоратора для ограничения доступа.**
# Напишите декоратор, который будет проверять, имеет ли пользователь                             
# доступ к выполнению определенной функции. Для простоты можно                             
# предположить, что у вас есть список пользователей с определенными                            
# правами. Если пользователь имеет право, функция выполняется;                                  
# в противном случае выводится сообщение об ошибке.


users = [{"name":"Alex", "rights": "False"},
         {"name":"Olga", "rights": "True"},
         {"name":"Macha", "rights": "True"},
         {"name":"Nasta", "rights": "True"},
         {"name":"Egor", "rights": "False"},
         {"name":"Vlad", "rights": "True"},
         {"name":"Pacha", "rights": "False"},
         {"name":"Vica", "rights":"False" },
         {"name":"Vacilica", "rights": "False"},
         {"name":"Marina", "rights": "True"}
         ]

def access_check_decorator(fun):
    def wrapper(users, name):
        for i in users:
            if i["rights"] == "True" and i["name"] == name:
                fun(users, name)
                break
        else:
            print("Denied eccess")
    return wrapper

name = input("Enter you name: ")


@access_check_decorator
def sguare_number(users, name):
    print(f"You are welcom {name}")
    
sguare_number(users, name)          


# **Создание декоратора с параметрами.**                     
# Напишите декоратор, который можно настроить с помощью параметров.                                
# Например, декоратор может принимать параметр n, который указывает                               
# максимальное количество раз, которое функция может быть вызвана.                            
# Если функция вызывается более n раз, декоратор должен выводить                               
# сообщение об ошибке.


# def limiting_calls_decorator(times):
#     my_file = open("count_file", "w+")
#     count = 0
#     def decorator(fun):
#         # my_file = open("count_file", "w+")
#         # count = 0
#         def wrapper(): 
#             nonlocal my_file 
#             nonlocal count
#             my_file.write(str(count))
#             if my_file.read() != times:
#                 fun()
#                 count += 1
#             else:
#                 print("time limiting")
#         return wrapper
#     return decorator

def counter_fun(time):
    def decorator(fun):
        counter = 0
        def wrapper():
            nonlocal counter 
            if counter != time:
                print("Numbers of function calls: ", counter)
                fun()
                counter += 1
            else:
                print("Time limit")
        return wrapper
    return decorator

@counter_fun(time = 4)
def square_number():
    try:
        number = int(input("Enter you number: "))
    except ValueError as e:
        print(e)
    print(number**2)

try:
    call_function = int(input("Enter numbers of function calls: "))
except ValueError as e:
    print("e")
for _ in range(call_function):
    square_number()


# **Задачи**

# 1) Написать рекурсию на вычисление факториала введённого числа                                

def recursia(n):
    if n == 1:
        return n
    else:
        return n * recursia(n-1)

print(recursia(int(input("Enter your number: "))))

# 2) Написать рекурсию на вычисление числа фибоначчи 

def fibonaci(n):
    if n <= 1:
        return n
    else:
        return fibonaci(n-1) + fibonaci(n-2)

# print(fibonaci(5))

# 3) Написать рекурсию на вычисление суммы элементов списка


def sum_list(list):
    if len(list) == 0:
        return 0
    else:
        return 1 + sum_list(list[1:])

print(sum_list([1,2,34]))


# # **Домашка**

# 1) Написать калькулятор с использованием замыканий.                       
# Калькулятор должен включать в себя все базовые математические                          
# операции, а так же квадратный корень и кубический корень чисел

def calculator(funс):
    def return_function(a, b):
        return funс(a, b)
    return return_function


def addition(a, b):
    return a + b

def deduction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def squadruple(a, b):
    return a ** b

def extractiong(a, b):
    return a ** (1 / b)

user_operetion = input("Enter operetion (1.addition, 2.deduction, 3.multiplication, 4.division, 5.squadruple, 6.extractiong): ").strip().lower()
try:
    a = int(input("Enter numer 1: "))
    b = int(input("Enter numer 2: "))
except ValueError as e:
    print(e)
match user_operetion:
    case "addition":
        yes = calculator(addition) 
        print(yes(a, b)) 
    case "deduction": print(calculator(deduction))
    case "multiplication": print(calculator(multiplication))
    case "division": print(calculator(division))
    case "squadruple": print(calculator(squadruple))
    case "extractiong": print(calculator(extractiong))
    case _: print("Function not found")