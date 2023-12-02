# Задача 1
# Реализуйте калькулятор из строки. Калькулятор включает в себя все базовые операции.
# Важно! Функцию eval() использовать запрещено.
# Пример: "20+15-30**2/90*7" -> -35



user_text = input("Enter your text: ")  
# user_text = "20+15-30**2/90*7"
number = ''
numbers = []
symbol = ''
symbols = []

try:
    for i in user_text:   
        if i in '0123456789':
            number += i
        elif number != '':
            numbers.append(int(number))
            number = ''
    else:
        numbers.append(int(number))
except ValueError as e:
    print(e) 
else:
    for i in user_text:   
        if i in '+-*/':
            symbol += i
        elif symbol != '':
            symbols.append(symbol)
            symbol = ''
    print(numbers, symbols)
    while "**" in symbols:
        for i in range(len(symbols)-1):
            if symbols[i] == '**':
                numbers[i] = numbers[i] ** numbers[i+1]
                numbers.pop(i+1)
                symbols.pop(i)

    while ("*" in symbols)  or ("/" in symbols): 
        symbols_count = len(symbols)
        for i in range(symbols_count):
            if symbols[i] == '*':
                numbers[i] = numbers[i] * numbers[i+1]
                numbers.pop(i+1)
                symbols.pop(i)
                break

            elif symbols[i] == '/':
                numbers[i] = numbers[i] / numbers[i+1]
                numbers.pop(i+1)
                symbols.pop(i)
                break

    while ("+" in symbols)  or ("-" in symbols):            
        symbols_count = len(symbols)
        for i in range(symbols_count):
            if symbols[i] == '+':
                numbers[i] = numbers[i] + numbers[i+1]
                numbers.pop(i+1)
                symbols.pop(i)
                break
            elif symbols[i] == '-':
                numbers[i] = numbers[i] - numbers[i+1]
                numbers.pop(i+1)
                symbols.pop(i)
                break 
    try:
        print(numbers[0])
    except IndexError as e:
        print(e)


# Задача 2
# Найдите все делители числа в списке.
# Список простых примеров: [4, 6, 16, 28].
# Список сложных примеров: [32456, 4356786, 34567897654].


# numbers = input("Enter the bunber with a cpase: ").strip().split()
# try:
#     numbers = [int(i) for i in numbers]
# except ValueError as e:
#     print(e)
numbers = [32456, 4356786, 34567897654]

divisions_elements = []
for element in numbers:
    divisions_element = []
    i = 1
    while i**2 <= element:
        if element % i == 0:
            divisions_element.append(i)
            if i != element // i:
                divisions_element.append(element // i)
        i += 1
    divisions_element.sort()
    divisions_elements.append(divisions_element)

for i in range(len(numbers)):
    print(f"Divisiors of numbers {numbers[i]}:", *divisions_elements[i], sep='\n')