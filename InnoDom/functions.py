# # **Практика**
# 1) Написать функцию, которая принимает произвольное количество                      
# аргументов и возвращает их среднее значение.


def averege_value(*arge):
    if len(arge)  == 0 :
        return 0
    result = sum(arge) / len(arge)
    return result
try:
    print(averege_value(*[float(i) for i in input("enter numbers: ").split()]))
except ValueError as e:
    print(e)


# 2) Написать функцию, которая принимает строку с паролем и возвращает                   
# **True**, если пароль соответствует определенным критериям безопасности,                
# и **False** в противном случае.
# **Критерии безопасности включают следующее:**
# **Длина пароля должна быть не менее 8 символов.**
# **Пароль должен содержать как минимум одну заглавную и одну строчную букву.**
# **Пароль должен содержать как минимум одну цифру и один символ.**
# Для упрощения задачи - что может входить в пароль
#   is_alnum_reg = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)"
#   symbol_reg = r"[!@#$%^&*?_|<>{}]"


import re

def password_verification(password):
    is_alnum_reg = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)"
    symbol_reg = r"[!@#$%^&*?_|<>{}]"
    if re.findall(symbol_reg, password) and re.match(is_alnum_reg, password):
        if len(password) >= 8:
            if password.lower() == password and password.upper() == password:
                return False
            else: 
                return True
        else:
            return False
    else:
        return False

print(password_verification(input("Enter you password: ")))


# 3) Есть список словарей, где каждый словарь представляет один                    
# продукт со следующими полями: `name`, `price` и `available`.
# Написать функцию, которая принимает этот список продуктов и возвращает                     
# новый список, содержащий только те продукты, которые есть в наличии                  
# и их цена не превышает 1000 рублей.


products = [
    {"name": "Smart TV", "price": 130, "available": True,},
    {"name": "Wireless Bluetooth Headphones", "price": 220, "available": False,},
    {"name": "Laptop", "price": 14, "available": True,},
    {"name": "Digital Camera", "price": 432, "available": False,},
    {"name": "Gaming Console", "price": 556, "available": True,},
    {"name": "Smartwatch", "price": 170, "available": False,},
    {"name": "Portable Bluetooth Speaker", "price": 130, "available": False,},
    {"name": "Drone", "price": 854, "available": True,},
    {"name": "Virtual Reality Headset", "price": 945, "available": False,},
    {"name": "Wireless Earbuds", "price": 1500, "available": True,},
    {"name": "Tablet", "price": 894, "available": True,},
    {"name": "Smart Home Security System", "price": 135, "available": False,},
    {"name": "Fitness Tracker", "price": 25, "available": True,},
    {"name": "External Hard Drive", "price": 659, "available": False,},
    {"name": "Bluetooth Keyboard", "price": 2654, "available": False,},
    {"name": "Noise-Canceling Headphones", "price": 819, "available": True,},
    {"name": "Action Camera", "price": 9511, "available": True,},
    {"name": "Wi-Fi Router", "price": 9156, "available": True,},
    {"name": "Gaming Mouse", "price": 123, "available": True,},
    {"name": "Wireless Charging Pad", "price": 10125, "available": False,},
    {"name": "Sofa bed", "price": 945, "available": True,},
    {"name": "Dining table", "price": 12, "available": False,},
    {"name": "Wardrobe", "price": 85, "available": False,},
    {"name": "Coffee table", "price": 73, "available": True,},
    {"name": "Recliner chair", "price": 856, "available": False,},
    {"name": "Bookcase", "price": 1500, "available": True,},
    {"name": "Bed frame", "price": 999, "available": True,},
    {"name": "Dressing table", "price": 12, "available": False,},
    {"name": "TV stand", "price": 3, "available": False,},
    {"name": "Ottoman", "price": 84, "available": True,},
]

def shopping(products):
    products_my = []
    for i in range(len(products)):
        if int(products[i]['price']) <= 1000 and products[i]['available']:
            products_my.append(products[i]['name'])
    return products_my

print("You shopping list: ", *shopping(products), sep = ', ')


# 4) Есть список словарей, где каждый словарь представляет                    
# один заказ со следующими полями: '`id`', '`table_number`' и '`bill`'.
# Написать функцию, которая принимает этот список заказов и                    
# возвращает новый список заказов, отсортированный по                
# возрастанию суммы заказа.     


orders = [
    {'id': 1, 'table_number': 5, 'bill': 25.50},
    {'id': 2, 'table_number': 10, 'bill': 42.75},
    {'id': 3, 'table_number': 3, 'bill': 15.20},
    {'id': 4, 'table_number': 8, 'bill': 37.90},
    {'id': 5, 'table_number': 2, 'bill': 10.50},
    {'id': 6, 'table_number': 12, 'bill': 55.80},
    {'id': 7, 'table_number': 6, 'bill': 29.95},
    {'id': 8, 'table_number': 9, 'bill': 41.10},
    {'id': 9, 'table_number': 4, 'bill': 19.75},
    {'id': 10, 'table_number': 7, 'bill': 34.60},
    {'id': 11, 'table_number': 1, 'bill': 8.25},
    {'id': 12, 'table_number': 11, 'bill': 50.40},
    {'id': 13, 'table_number': 5, 'bill': 25.00},
    {'id': 14, 'table_number': 10, 'bill': 43.25},
    {'id': 15, 'table_number': 3, 'bill': 16.80},
    {'id': 16, 'table_number': 8, 'bill': 38.50},
    {'id': 17, 'table_number': 2, 'bill': 11.75},
    {'id': 18, 'table_number': 12, 'bill': 56.20},
    {'id': 19, 'table_number': 6, 'bill': 30.50},
    {'id': 20, 'table_number': 9, 'bill': 42.90},
    {'id': 21, 'table_number': 4, 'bill': 20.25},
    {'id': 22, 'table_number': 7, 'bill': 35.10},
    {'id': 23, 'table_number': 1, 'bill': 9.75},
    {'id': 24, 'table_number': 11, 'bill': 51.60},
    {'id': 25, 'table_number': 5, 'bill': 25.50},
    {'id': 26, 'table_number': 10, 'bill': 42.75},
    {'id': 27, 'table_number': 3, 'bill': 15.20},
    {'id': 28, 'table_number': 8, 'bill': 37.90},
    {'id': 29, 'table_number': 2, 'bill': 10.50},
    {'id': 30, 'table_number': 12, 'bill': 55.80}
]

def corted_orders(orders):
    sorted_dict = sorted(orders, key = lambda d: d['bill'])
    return sorted_dict
print("New dict: ", corted_orders(orders))


# 5) Есть список словарей, где каждый словарь представляет                
# одного клиента со следующими полями: '`id`', '`name`', '`age`' и '`sex`'.                       
# Написать функцию, которая принимает этот список клиентов и                 
# возвращает количество женщин в списке.                   


clients = [
    {'id': 1, 'name': 'Alice', 'age': 32, 'sex': 'Female'},
    {'id': 2, 'name': 'Bob', 'age': 45, 'sex': 'Male'},
    {'id': 3, 'name': 'Charlie', 'age': 28, 'sex': 'Male'},
    {'id': 4, 'name': 'David', 'age': 54, 'sex': 'Male'},
    {'id': 5, 'name': 'Eva', 'age': 39, 'sex': 'Female'},
    {'id': 6, 'name': 'Frank', 'age': 42, 'sex': 'Male'},
    {'id': 7, 'name': 'Grace', 'age': 61, 'sex': 'Female'},
    {'id': 8, 'name': 'Henry', 'age': 50, 'sex': 'Male'},
    {'id': 9, 'name': 'Isabella', 'age': 26, 'sex': 'Female'},
    {'id': 10, 'name': 'Jack', 'age': 33, 'sex': 'Male'},
    {'id': 11, 'name': 'Kate', 'age': 49, 'sex': 'Female'},
    {'id': 12, 'name': 'Liam', 'age': 23, 'sex': 'Male'},
    {'id': 13, 'name': 'Mia', 'age': 37, 'sex': 'Female'},
    {'id': 14, 'name': 'Noah', 'age': 58, 'sex': 'Male'},
    {'id': 15, 'name': 'Olivia', 'age': 41, 'sex': 'Female'},
    {'id': 16, 'name': 'Peter', 'age': 31, 'sex': 'Male'},
    {'id': 17, 'name': 'Quinn', 'age': 56, 'sex': 'Female'},
    {'id': 18, 'name': 'Ryan', 'age': 35, 'sex': 'Male'},
    {'id': 19, 'name': 'Sophia', 'age': 47, 'sex': 'Female'},
    {'id': 20, 'name': 'Thomas', 'age': 29, 'sex': 'Male'},
    {'id': 21, 'name': 'Uma', 'age': 60, 'sex': 'Female'},
    {'id': 22, 'name': 'Victoria', 'age': 44, 'sex': 'Female'},
    {'id': 23, 'name': 'William', 'age': 52, 'sex': 'Male'},
    {'id': 24, 'name': 'Xavier', 'age': 36, 'sex': 'Male'},
    {'id': 25, 'name': 'Yara', 'age': 30, 'sex': 'Female'},
    {'id': 26, 'name': 'Zoe', 'age': 43, 'sex': 'Female'},
    {'id': 27, 'name': 'Alex', 'age': 27, 'sex': 'Male'},
    {'id': 28, 'name': 'Benjamin', 'age': 48, 'sex': 'Male'},
    {'id': 29, 'name': 'Chloe', 'age': 38, 'sex': 'Female'},
    {'id': 30, 'name': 'Daniel', 'age': 55, 'sex': 'Male'}
]


def count_women(clients):
    count = 0
    for i in range(len(clients)):
        if clients[i]['sex'] == 'Female':
            count += 1
    return count

print("Women: ", count_women(clients))


# 6) Работаем над системой анализа текста.
# Написать функцию, которая принимает текстовую строку и список                     
# стоп-слов (слов, которые не несут смысловой нагрузки \ оскорбления \ "нежелательные"),                    
# и возвращает новую строку, в которой удалены все стоп-слова                           
# из исходного текста


import re

def deled_wolds(user_text, *wolds_delet):
    for i in wolds_delet:
        user_text = user_text.replace(i, '')
    user_text = re.sub(' +', ' ', user_text)
    if user_text == '':
        print("You didn't text or/and wolds!")
    return user_text
user_text = input("Enter you text: ")
wolds_for_delet = input("Enter wolds to be deleted: ")
print(deled_wolds(user_text, *wolds_for_delet.split()))

    