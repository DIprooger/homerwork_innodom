# Задача 1
# Сформировать стек целых чисел, вводимых пользователем, а затем его содержимое вывести на экран.


from collections import deque

numbers_stack = deque()
try:
    count = int(input("Enter the of characters to be entered: "))
    for _ in range(count):
        numbers_stack.append(int(input("Enter your number: ")))
except ValueError as e:
    print(e)
else:
    print(*numbers_stack)


# Задача 2
# Элементы целочисленного списка записать в очередь. Написать функцию извлечения элементов из очереди до тех пор,
# пока первый элемент очереди не станет чётным.

  
number_queue = deque()
try:
    user_numbers = list(map(int, input("Enter your number: ").strip().split()))
except ValueError as e:
    print(e)
for i in user_numbers:
    number_queue.append(i)
for i in user_numbers:         #почему не работает когда вместо user_numbers - number_queue?
    if not(i % 2 == 0):
        number_queue.popleft()
    else:
        break
print(number_queue)

    
# Задача 3
# Даны две непустые очереди [1, 2, 5, 6] и [3, 4, 7]. Элементы каждой из очередей упорядочены по возрастанию. 
# Объединить очереди в одну, с сохранением упорядоченности элементов.


sotred_number = deque()
first_list = [1, 2, 5, 6]
second_list = [3, 4, 7]
same = set(first_list) & set(second_list)
for _ in range(len(first_list) + len(second_list) - len(same)):   
    if len(first_list) == 0:
        sotred_number.append(second_list[0])
        second_list.pop(0)
    elif len(second_list) == 0:
        sotred_number.append(first_list[0])
        first_list.pop(0)
    elif first_list[0] == second_list[0]:       # обработка случая если элементы одинаковые
        sotred_number.append(first_list[0])
        second_list.pop(0)
        first_list.pop(0)
    elif first_list[0] < second_list[0]:
        sotred_number.append(first_list[0])
        first_list.pop(0)
    elif first_list[0] > second_list[0]:
        sotred_number.append(second_list[0])
        second_list.pop(0)
    
print(sotred_number)


# Задача 4
# Расположить элементы целочисленного списка [1, 2, 3, 4, 5, 6, 7] в обратном порядке с использованием стека.


numbers = deque()
user_numbers = [1, 2, 3, 4, 5, 6, 7]
for i in user_numbers[::-1]:
    numbers.append(i)
print(numbers)


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