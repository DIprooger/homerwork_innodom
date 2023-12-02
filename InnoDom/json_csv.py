# Есть файл с данными о пассажирах Титаника.
# Выведите общее количество пассажиров, представленных в данных.


import json


with open("titanic_data.json", "r") as titanic:
    titanic = json.load(titanic)

# print("Of the piple on the Titanic:", len(titanic))


# Из этого же файла нужно забрать информацию:
# 1) всех пассажиров                            ЧТО значит забрать информацию всех посажиров? мы может 
# 2) Количество выживших и их имена             прочитать и передать переменной информацию. это тоже самое?
# 3) Количество умерших пассажиров и их имена.


# dead = []
# alive = []
# for passenger in titanic:
#     if passenger["Survived"] == 0:
#         dead.append(passenger["Name"])
#     else:
#         alive.append(passenger["Name"])

# print("Dead:", len(dead))
# print("Name:", "\n ".join(dead))
# print("Dead:", len(alive))
# print("Name:", "\n ".join(alive))


# Найти самого пожилого пассажира. Вывести его имя, возраст и класс каюты.


# age = 0
# name = ''
# cabin = ''

# for passenger in titanic:
#     age_passenger = passenger["Age"] 
#     if age_passenger == '':
#         continue
#     if age < float(age_passenger):
#         age = age_passenger
#         name = passenger["Name"]
#         cabin = passenger["Cabin"]

# print("The oldest passenfer on the Titanic was:", name)
# print("Age:", age)
# print("Cabin:", cabin)


# Выведите список имен всех пассажиров, чей возраст в диапазоне от 20 до 50 лет
# и класс пассажира - 2-ой.

# name_passenger = []
# for passenger in titanic:
#     age = passenger["Age"]
#     p_class = passenger["Pclass"]
#     if age == '':
#         continue
#     if 20 < float(age) <= 50 and int(p_class) == 2:
#         name_passenger.append(passenger["Name"])

# print("Passenger between the ages of 20 and 50:\n", "\n ".join(name_passenger))


# В файле titanic.csv подсчитать общее кол-во мужчин, женщин и детей(до 15 лет включительно)


import csv

# mans = []
# womans = []
# kids = []

# with open("titanic.csv", "r") as titanic:
#     titanic = csv.DictReader(titanic)

#     for passenger in titanic:
#         age = passenger["Age"]
#         name = passenger["Name"]
#         sex = passenger["Sex"]

#         if age == '':
#             continue
#         if float(age) > 15:
#             if sex == "male":
#                 mans.append(name)
#             else:
#                 womans.append(name)
#         else:
#             kids.append(name)

# print("Name mans:\n", "\n".join(mans))
# print()
# print()
# print("Name womans:\n", "\n".join(womans))
# print()
# print()
# print("Name kids:\n", "\n".join(kids))


# Найти средний возраст пассажиров в зависимости от класса билетов.

# age_1 = []
# age_2 = []
# age_3 = []

# with open("titanic.csv", "r") as titanic:
#     titanic = csv.DictReader(titanic)

#     for passenger in titanic:
        
#         age = passenger["Age"]
#         if age == '':
#             continue
#         p_class = int(passenger["Pclass"])
#         if p_class == 1:
#             age_1.append(float(age))
#         elif p_class == 2:
#             age_2.append(float(age))
#         else:
#             age_3.append(float(age))

# print("average age of passengers class 1:", round(sum(age_1)/len(age_1), 1))
# print("average age of passengers class 2:", round(sum(age_2)/len(age_2), 1))
# print("average age of passengers class 3:", round(sum(age_3)/len(age_3), 1))


# Определить процент выживших мужчин, женщин и детей (ребёнком                    
# считается пассажир до 15-ти лет включительно)

mans = 0
mans_alive = 0
womans = 0
womans_alive = 0
kids  = 0
kids_alive = 0

with open("titanic.csv", "r") as titanic:
    titanic = csv.DictReader(titanic)

    for passenger in titanic:
        age = passenger["Age"]
        sex = passenger["Sex"]
        dead_or_alive = int(passenger["Survived"])

        if age == '':
            continue
        if float(age) > 15:
            if sex == "male":
                mans += 1
            else:
                womans += 1
        else:
            kids += 1
        
        if float(age) > 15 and dead_or_alive == 1:
            if sex == "male":
                mans_alive += 1
            else:
                womans_alive += 1
        elif dead_or_alive == 1:
            kids_alive += 1

print("Percentage of survivors by gender and age")
print("The percentage of femal survivors:", round(womans_alive / womans * 100), "%")
print("The percentage of male survivors:", round(mans_alive / mans * 100), "%")
print("The percentage of kids survivors:", round(kids_alive / kids * 100), "%")
print("the percentage of survivors out of the total")
print("The percentage of femal survivors:", round(len(passenger)/womans_alive * 100), "%")
print("The percentage of male survivors:", round(len(passenger)/mans_alive   * 100), "%")
print("The percentage of kids survivors:", round(len(passenger)/kids_alive   * 100), "%")


# Распределить всех пассажиров по портам посадки:
# Значения могут быть:                # Этих пассажиров распределить по:
# "S" (Southampton),                  # мужчинам
# "C" (Cherbourg)                     # женщинам
# "Q" (Queenstown)                    # детям (до 15 лет включительно)
# Выходные данные записать в новый csv файл

# class_s = []
# class_c = []
# class_q = []

# with open("titanic.csv", "r") as titanic:
#     titanic = csv.DictReader(titanic)
#     for passenger in titanic:
#         embarked = passenger["Embarked"]
#         if embarked == "S":
#             class_s.append(passenger)
#         elif embarked == "C":
#             class_c.append(passenger)
#         elif embarked == "Q":
#             class_q.append(passenger)

# def sorted_titanic(dict_my):
#     mans = []
#     womans = []
#     kids = []
#     for element in dict_my:
#         sex = element["Sex"]
#         age = element["Age"]
#         if age == '':
#             continue
#         if float(age) > 15:
#             if sex == "male":
#                 mans.append(element)
#             else:
#                 womans.append(element)
#         else:
#             kids.append(element)
#     result = mans + womans + kids
#     return result


# class_c = sorted_titanic(class_c)
# class_s = sorted_titanic(class_s)
# class_q = sorted_titanic(class_q)

# with open("titanic_c.csv", "w") as titanic_c:
#     fielname = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
#     write = csv.DictWriter(titanic_c, fieldnames=fielname)
#     write.writeheader()
#     write.writerows(class_c)

# with open("titanic_s.csv", "w") as titanic_s:
#     fielname = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
#     write = csv.DictWriter(titanic_s, fieldnames=fielname)
#     write.writeheader()
#     write.writerows(class_s)

# with open("titanic_q.csv", "w") as titanic_q:
#     fielname = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
#     write = csv.DictWriter(titanic_q, fieldnames=fielname)
#     write.writeheader()
#     write.writerows(class_q)