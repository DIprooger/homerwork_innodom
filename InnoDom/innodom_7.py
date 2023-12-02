# Задача 1 Создайте переводчик, который переводит слова с 
# русского на английский и наоборот. Пользователь вводит 
# слово, нужно перевести его на другой язык. Если такого 
# слова не существует в словаре, выведите на экран “нет такого слова”.


Translate_dict = {
   "people":"люди",
   "family":"семья",
   "woman":"женщина",
   "man":"мужчина",
   "girl":"девочка",
   "boy":"мальчик",
   "child":"ребёнок",
   "friend":"друг",
   "husband":"муж",
   "wife":"жена",
   "name":"имя",
   "head":"голова",
   "face":"лицо",
   "hand":"рука",
   "life":"жизнь",
   "hour":"час",
   "week":"неделя",
   "day":"день",
   "night":"ночь",
   "month":"месяц",
   "year":"год",
   "time":"время",
   "world":"мир",
   "sun":"солнце",
   "animal":"животное",
   "tree":"дерево",
   "water":"вода",
   "food":"еда",
   "fire":"огонь",
   "country":"страна",
   "city":"город",
   "street":"улица",
   "work":"работа",
   "school":"школа",
   "shop":"магазин",
   "house":"дом",
   "room":"комната",
   "car":"машина",
   "paper":"бумага",
   "pen":"ручка",
   "door":"дверь",
   "chair":"стул",
   "table":"стол",
   "money":"деньги",
   "way":"путь",
   "end":"конец",
   "price":"цена",
   "question":"вопрос",
   "answer":"ответ",
   "number":"номер"
}

user_wold = input("Enter wolf for traslait: ")
keys = list(Translate_dict.keys())

for i in Translate_dict.values():
    if i == user_wold:
        index = list(Translate_dict.values()).index(user_wold)
        print("Result transleit:", keys[index])
        break       
else:
    print("Result transleit:", Translate_dict.get(user_wold, "Not faund!"))



# Задача 2
# 1кг творога стоит 5 руб. Выведите на экран таблицу стоимости творога массой
# 100г, 200г, 300г, 600г, 900г


price_curd = {}
for i in range(100, 1000, 100):
    price_curd[i] = .005 * i
del price_curd[400]
del price_curd[500]
del price_curd[700]
del price_curd[800]
print(price_curd)