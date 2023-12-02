# **`
# 7) Есть код, который написал какой-то другой разработчик, мало того, что                    
# там нет типизации, не особо понятно что где лежит, так ещё и странный порядок                   
# глобальных значений и функций, логика не работает.                          
# В реальной разработке вы будете сталкиваться с чужим кодом, который может                          
# работать некорректно \ не работать вообще. Как будущие специалисты                    
# вы должны уметь разбираться в чужом коде так же, местами его переписывать,                   
# если это необходимо.                            
# Проанализируйте код, поймите почему он не работает, перепишите так, чтобы                              
# необходимые действия выполнялись.                            


import json
from typing import Callable

def read_data_from_file(fille):
    """_summary_

    Args:
        fille (str): _description_

    Returns:
        _type_: _description_
    """
    with open(fille, "r") as fille_read:
        data = json.load(fille_read)
    return data

def get_passenger(data):
    p_id = 2
    for element in data:
        if element["PassengerId"] == p_id:
            return element
        
def write_filtered_data_into_file(data):
    new_fille = "passenger_with_id_2.json"
    with open(new_fille, "w") as target:
        json.dump(data, target, indent=4)

def comand(file_actions, data):
    result = None
    match file_actions:
        case "eceive": 
            result = read_data_from_file(data),
        case "poisk": 
            result = get_passenger(data),
        case "write": 
            write_filtered_data_into_file(data),
    return result

def process(vybor: str, data=None) -> Callable:
    """the function accepts a string. 
       This string is compared with the values. And depending on the value, 
       it calls a function that passes arguments.

    Args:
        vybor (str): 

    Returns:
        _type_: _description_
    """
    filename = "titanic_data.json"

    match vybor:
        case "receive":
            return comand("receive", filename)
        case "poisk":
            return comand("poisk", data)
        case "write":
            comand("write", data)
            return None
        case _:
            print("No matches")
            return None

us_inp =" "
data = None 
print("To end the program press q.")
while us_inp != "q":
    us_inp = input("Enter your action with file: ")
    process(us_inp)