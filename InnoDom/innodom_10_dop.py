# Задача
# Из файла stars.txt, приложенного к занятию:
# 1. Запишите данные в бинарный файл


import pickle, json, os

with open("stars.txt", "r") as stars, open("satrs.picle", "wb") as stars_picle:
    read = stars.read()
    stars = pickle.dump(read, stars_picle)


# 2. Сделайте копию бинарного файла в другом расширении


with open("satrs.picle", "rb") as stars_picle:
    stars = pickle.load(stars_picle)

with open("satrs.json", "w", encoding="utf-8") as stars_json:
    json.dump(stars, stars_json)


# 3. Удалите файл из пункта 1


path = "satrs.picle"
os.remove(path)


# 4. Прочитайте копию и выведите данные на экран


with open("satrs.json", "r", encoding="utf-8") as stars_json:
    read = json.load(stars_json)
print(read)