# Задача 1
# Из приложенного к уроку json-файла, заберите данные и переместите их в таблицу csv, 
# в удобном для вас виде.

import csv, json

with open("films.json", "r") as films:
    json_films = json.load(films)["films"]

with open("films.csv", "w") as films:

    field_names = ['name', 'release', 'producer', 'IMDb', 'metacritic', 'rottentomatoes', 'actors']
    writer = csv.DictWriter(films, fieldnames=field_names)
    writer.writeheader()
    new_move = []

    for element in json_films:
        new_dict_move = dict()
        new_dict = dict()
        new_string = ''
        new_dict_str = dict()

        for i in element:
            if i == 'evaluations':
                evaluations = element['evaluations']
                for element_evaluations in evaluations:
                    new_dict[element_evaluations["name"]] = element_evaluations['result']
            elif i == 'actors':
                for name in element["actors"]:
                    new_string += name + ', '
                new_dict_str[i] = new_string
            else:  
                new_dict_move[i] = element[i]
        new_move.append(new_dict_move|new_dict|new_dict_str)
    
    for i in new_move:
        writer.writerow(i)

       
# print()
# Задача 2
# Из приложенного к уроку json-файла, заберите данные и запишите в 
# .txt те фильмы, в которых рейтинг по IMDb меньше 8.5


with open("films.csv", "r") as films, open("films.txt", "w") as fims_txt:
    reader = csv.DictReader(films)
    for element in reader:
        if element['IMDb'] < '8.5':
            fims_txt.writelines(str(element)+'\n')

with open("films.json", "r") as films, open("films_hard.txt", "w") as fims_txt:
    json_films = json.load(films)["films"]
    for element in json_films:
        evaluations = element['evaluations']
        for name in evaluations:
            if name['name'] == 'IMDb' and name['result'] < 8.5:
                fims_txt.write(str(element) + '\n')          
