# Задача 1
# Напишите функцию, которая рекурсивно считает сумму чисел в списке.

numbers = input("Enter numbers with the spase: ").split()
try:
    numbers = [int(i) for i in numbers]
except ValueError as e:
    print(e)

def summ_numbers(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + summ_numbers(numbers[1:])

print(summ_numbers(numbers))

# Задача 2
# Напишите функцию для проверки, совершенное ли число.
## как можно ещё сильнее уменьшить время выполнения кода? на больших числа долго работает

try:
    number = int(input("Enter your number: "))  
except ValueError as e:
    print(e)

def perfect_numbers(number):
    divisions_element = []
    i = 1
    for_delet = number
    while i**2 <= number:
        if number % i == 0:
            divisions_element.append(i)
            if i != number // i:
                divisions_element.append(number // i)
        i += 1
    divisions_element.remove(for_delet)
    
    if sum(divisions_element) == number:
        print("Yes, the number is perfect")
    else:
        print("No, the number isn't perfect")

perfect_numbers(number)


# Задача 3
# Напишите функцию для проверки, простое ли число.


def simple_number(number):
    if number == 1 or number == 0:
        return print("The numbet isn't simple")
    elif number == 2 or number == 3:
        return print("The numbet is simple")
    elif number % 2 == 0 or number % 3 == 0:
        return print("The numbet isn't simple")
    else:
        i = 1
        while i**2 <= number:
            if number % (6*i + 1) == 0 or number % (6*i - 1) == 0:
                return print("The numbet isn't simple")
            i += 1
    return print("The numbet is simple")

try:
    number = int(input("Enter your number: "))  
except ValueError as e:
    print(e)

simple_number(number)
