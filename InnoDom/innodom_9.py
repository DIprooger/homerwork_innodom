# Задача 1
# Напишите программу, которая находит все отрицательные числа. Ввод и вывод организуйте с помощью файлов.

with open("numbers.txt", "w") as numbers:
    numbers_user = input("Enter numbers with a space: ")
    numbers.writelines(numbers_user)

with open("numbers.txt", "r") as numbers, open("negative_numbers.txt", "w") as negative_numbers:
    my_number = numbers.read().split()
    count = 0
    for i in my_number:
        if float(i) < 0:
            count += 1
            negative_numbers.write(str(i) + ' ')
    if count == 0:
        negative_numbers.write("There are no negative numbers")

with open("negative_numbers.txt", "r") as negative_numbers:
    print(negative_numbers.read())

    
# Задача 2
# Напишите программу, которая объединяет строки из двух файлов и записывает результат в третий файл. 
# Количество строк в файлах может быть разное.

with open("firx_text.txt", "w", encoding="utf-8") as first, open("second_text.txt", "w", encoding="utf-8") as second:
    first.write(
"""Равным образом постоянный количественный рост и сфера нашей активности обеспечивает широкому кругу 
(специалистов) участие в формировании системы обучения кадров, соответствует насущным потребностям. 
Таким образом реализация намеченных плановых заданий в значительной степени обуславливает создание новых предложений. 
С другой стороны постоянный количественный рост и сфера нашей активности в значительной степени обуславливает создание 
модели развития. Задача организации, в особенности же сложившаяся структура организации в 
значительной степени обуславливает создание соответствующий условий активизации.""")
    
    second.write(
"""Повседневная практика показывает, что консультация с широким активом обеспечивает широкому кругу (специалистов) 
участие в формировании существенных финансовых и административных условий. Задача организации, в особенности же новая 
модель организационной деятельности требуют определения и уточнения форм развития.""")

with open("text.txt", "w", encoding="utf-8") as text, open("firx_text.txt", "r", encoding="utf-8") as first, open("second_text.txt", "r", encoding="utf-8") as second:
    finich_text = first.read() + second.read()
    text.write(finich_text)
    
