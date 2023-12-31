#**Шифрование строки:**
#Пользователь вводит строку. Преобразовать каждый
#символ этой строки в его байтовое представление. Затем вывести
#байты на экран.

input_text = input('Введите текс для перевода в байтовое представление: ')
byte_text = bytes(input_text, 'utf-8')
print(byte_text)


#**Реверсирование слов:**
#Пользователь вводит предложение. Инвертировать
#порядок слов в предложении (не меняя порядок букв в словах) и
#вывести измененное предложение.

user_line = input('Введите текст для прочтения с конца: ').split()
print(*user_line[::-1])


#**Поиск наибольшего слова:**
#Пользователь вводит предложение. Найти самое длинное
#слово в предложении и вывести его.

your_text = input('Введите текст для поиска самого длиного слова: ').split()
max_world = max(your_text, key = len)
print(max_world)


#**Сложение чисел в строке:**
#Пользователь вводит строку, содержащую несколько чисел,
#разделенных пробелами. Найти сумму всех чисел в этой строке и
#вывести результат.

user_numbers = [int(i) for i in input('Введите числа через пробел: ').split()]
гыг = list(map(int, input('Введите числа через пробел: ').split()))
print(sum(гыг))
print(sum(user_numbers))


#**Сортировка слов в предложении:**
#Пользователь вводит предложение. Отсортировать
#слова в предложении в алфавитном порядке и вывести результат.

user_input = input('Введите текст для сортировки через пробел: ').split()
print(*sorted(user_input))