# Задача 1
# Написать программу, которая создаёт папку. Далее создаёт ещё две папки в этой же папке, 
# а в каждой из папок - по одному текстовому файлу. А затем переименовывает корневую папку.

import os

path = os.getcwd()
name = input("Enter name directiri: ")

os.mkdir(rf"{path}\\{name}")
os.mkdir(rf"{path}\\{name}\\first")

with open(rf"{path}\\{name}\\first\\first.text", "w") as first:
    first.write("Hello! I'm first file")

os.mkdir(rf"{path}\\{name}\\second")

with open(rf"{path}\\{name}\\second\\second.text", "w") as second:
    second.write("Hello! I'm secomd file")

yes_or_no = input(f"Do you want rename the directory {name}? (yes/no): ")
while yes_or_no != 'no':
    if yes_or_no == "yes":
        name_nawe = input("Enter name directiri: ")
        os.rename(rf"{path}\\{name}", rf"{path}\\{name_nawe}")
        os.rename(rf"{path}\\{name}\\first", rf"{path}\\{name_nawe}\\first")
        os.rename(rf"{path}\\{name}\\first\\first.text", rf"{path}\\{name_nawe}\\first\\first.text")
        os.rename(rf"{path}\\{name}\\second", rf"{path}\\{name_nawe}\\second")
        os.rename(rf"{path}\\{name}\\second\\second.text", rf"{path}\\{name_nawe}\\second\\second.text")
    yes_or_no = input(f"Do you want rename the directory {name}? (yes/no)")
    

# Задача 2
# Выведите содержимое любой папки на вашем диске.


path = os.getcwd()
print(os.listdir(path=""))
print("To exit, write no.")
open_user= ''
while open_user != "no":
    open_user = input(f"Which folder shuold i open: ")
    path += f"\\{open_user}"
    if os.path.isdir(f"{path}"):
        os.chdir(open_user)
        print(os.listdir(path=""))
        
    elif os.path.isfile(f"{path}"):      
        with open(path, "r", encoding="utf-8") as path:      
            print(path.read()) 
    
    else:
        print("not found")
print("end")      