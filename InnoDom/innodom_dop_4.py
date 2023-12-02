# Задача 1
# Создайте список с числами, переведите этот список в массив array и обратно в список.


import array

try:
    input_numbers = [int(i) for i in input("Enter the numers with a space: ").split()]
    numbers = array.array('b', input_numbers)
    print(numbers)
    list_number = numbers.tolist()
    print(list_number)
except ValueError as e:
    print(e)
except NameError as e:
    print(e)


# Задача 2
# Создайте массив array с значениями от 1 до 10000. Переведите этот массив в массив байтов.


my_array = array.array('q', [i for i in range(1, 10001)]) 
my_array_byttes = my_array.tobytes()
print(my_array)
print(my_array_byttes)


# Задача 3
# Создайте 3 массива с числами от 10 до 100 с разными типами. В каждом массиве выведите
# его тип, размер в байтах 1 элемента и информацию: ячейка памяти, длина.


my_array_1 = array.array('b', [i for i in range(10, 101)])  
my_array_2 = array.array('f', [i for i in range(10, 101)])  
my_array_3 = array.array('d', [i for i in range(10, 101)]) 
print(type(my_array_1[0]), my_array_1.itemsize, my_array_1.buffer_info())
print(type(my_array_2[0]), my_array_2.itemsize, my_array_2.buffer_info())
print(type(my_array_3[0]), my_array_3.itemsize, my_array_3.buffer_info())


# Задача 4
# Пользователь вводит 2 числа — это диапазон, требуется создать список на эти числа.
# Есть массив array [1,2,3,4,5,6,7,8,9,10]. Расширьте массив значениями из сгенерированного списка.


try:
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))
    user_numbers = [i for i in range(start, end + 1)]
    my_array = array.array('b', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    my_array.fromlist(user_numbers)
    print(my_array)
except ValueError as e:
    print(e)
except NameError as e:
    print(e)
except MemoryError as e:
    print(e)