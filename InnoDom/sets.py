# 4) Создайте два множества odd_numbers и even_numbers, содержащих нечетные              
# и четные числа от 1 до 10 соответственно. Попросите пользователя ввести             
# число и выведите "Четное" или "Нечетное" в зависимости от того,                       
# в каком множестве оно находится.


even_numbers = list(range(2, 11, 2))  
odd_numbers = list(range(1, 11, 2)) 
try:
    user_number = int(input("Enter your number: "))
except ValueError as e:
    print(e)
if user_number in even_numbers:
    print("Even number!")
elif user_number in odd_numbers:
    print("Odd number!")
else:
    print("number greater than 10")


# 5) Создайте два множества set_a и set_b, содержащих различные элементы.                         
# Если хотя бы один из них меньше трёх элементов(включительно), объедините                               
# их в одно множество и выведите его содержимое.


# set_a = set(input("Enter: "))
# set_b = set(input("Enter: "))

# if (len(set_a) <= 3 or len(set_b)) <= 3 and len(set_a | set_b) != 0:
#     print(set_a | set_b)
# elif len(set_a) == 0 and len(set_b) == 0:
#     print("Nothing enter")
# else:
#     print("Each set is greater than 3 elements")


# 1) Создайте словарь **student_grades**, где ключами будут имена студентов,            
# а значениями - их оценки (целые числа). Запросите у пользователя имя            
# студента и выведите его оценку. Если студент не найден в словаре,           
# выведите "Студент не найден".


# student_grades = {
#     "Den" : 4,
#     "Blad" : 10,
#     "Klaus" : 9
# }
# user_name = input("Enter name: ")
# print(student_grades.get(user_name, "Studen not found"))


# 2) Создайте словарь **inventory** с товарами и их количеством в магазине.             
# Попросите пользователя ввести название товара и проверьте, есть ли этот               
# товар в словаре. Если товар не найден, установите для этого товара значение          
# 4 по умолчанию.


# inventory = {
#     "Milk" : 3,
#     "Bread" : 45,
#     "Meat" : 34
# }
# user_products = input("Enter ptoducts: ")
# inventory.setdefault(user_products, 4)
# print(inventory)


# 3) Создайте два словаря **english_words** и **spanish_words** с переводами английских            
# и испанских слов. Попросите пользователя ввести слово на английском и             
# выведите его перевод на испанский. Если слово не найдено, выведите           
# "Перевод не найден".

##вариант 0 с иереводом из английского в испанский и наоборот.
# spanish_words = {
#     "Butterfly": "Mariposa",
#     "Training": "Formación",
#     "Restaurant": "Restaurante",
#     "Programming": "Programación",
# }

# english_words = {
#     "Butterfly": "Mariposa",
#     "Training": "Formación",
#     "Restaurant": "Restaurante",
#     "Programming": "Programación",
# }
# english_or_spanish = input("Enter english(en) or spanish(sp) world for translation: ").strip().lower()
# if english_or_spanish == "en" or english_or_spanish == "english":
#     print(spanish_words.get(input("Enter english world: "), "Translation not found"))
# elif english_or_spanish == "sp" or english_or_spanish == "spanish":   
#     print(english_words.get(input("Enter spanish world: "), "Translation not found"))

spanish_words = {
    "Бабочка": "Mariposa",
    "Обучение": "Formación",
    "Ресторан": "Restaurante",
    "Программирование": "Programación",
}

english_words = {
    "Butterfly": "Бабочка",
    "Training": "Обучение",
    "Restaurant": "Ресторан",
    "Programming": "Программирование",
}

english = input("Enter english(en) world for translation: ").strip()
print(spanish_words.get(english_words.get(english, "not faind"), "not faind"))

# 4) Создайте словарь **phone_book** с именами контактов и их номерами телефонов.            
# Попросите пользователя ввести имя контакта и выведите его номер.            
# Если контакт не найден, спросите пользователя, хочет ли он создать новый контакт.            
# Если да - создайте новый ключ с номером телефона, который пользователь должен          
# будет ввести. Если нет - прекратить работу.


# book_contact = {
#     "Andrey": "+1234568789",
#     "Irina": "+793545613254",
#     "Nikita": "+995557003215",
#     "Alex": "789456123121",
# }

# name = input("Enter name:")
# user_name_book = book_contact.get(name, False)
# if not(user_name_book):
#     ansver = input("Create a new contact yes or no: ").strip().lower()
#     if ansver == "yes":
#         book_contact.setdefault(name, input("Enter number: "))
#         print(book_contact)
#     else:
#         print("Search is over")
# else:
#     print(user_name_book)
    