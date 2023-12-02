# Задача 1
# Пользователь вводит количество символов a и b стороны прямоугольника. Требуется напечатать такой прямоугольник.


try:
    a = int(input("Enter length: ")) 
    b = int(input("Enter height: ")) 
except ValueError as e:
    print(e)

print("-" * a)
for i in range(b-2):
    print("-", " " * (a - 4), "-")
print("-" * a)


# Задача 2
# Пользователь вводит числа в список. Требуется вывести все числа, которые имеют делитель в этом списке.


user_number = input("Enter the number wich spase: ").split()
user_number = [int(i) for i in user_number]
resul = set()
for i in user_number:
    new_number = user_number.copy()
    new_number.remove(i)
    print(new_number)
    for j in new_number:
        if i % j == 0:
            print(i, j)
            resul.add(i)
            break

print("These number(s) have a divisor in the list:", resul)