# # **Homework**

# 1) Есть список с объектами в виде учеников:                   
# Вывести всех студентов мужского пола и женского пола отдельно.                  
# Посчитать их количество(сколько парней и сколько девушек)                    
# Вывести всех старше 20-ти лет                              
# Вывести имена только тех студентов, кто учится на                            
# математическом факультете 

university_students = [
    {
        "name": "Alex",
        "age": 19,
        "sex": "man",
        "facultet": "math"
    },
    {
        "name": "Ban",
        "age": 18,
        "sex": "man",
        "facultet": "math"
    },
    {
        "name": "Chloe",
        "age": 22,
        "sex": "woman",
        "facultet": "physics"
    },
    {
        "name": "Sasha",
        "age": 21,
        "sex": "woman",
        "facultet": "pcyology"
    },
    {
        "name": "Adam",
        "age": 27,
        "sex": "man",
        "facultet": "biology"
    },
    {
        "name": "Lesya",
        "age": 21,
        "sex": "woman",
        "facultet": "pcyology"
    },
    {
        "name": "Linda",
        "age": 23,
        "sex": "woman",
        "facultet": "geography"
    }
]
                      
woman = []
man = []
count_woman = 0
count_man = 0
more_than_20 = []
math = []

for element in university_students:
    if element["sex"] == "woman":
        count_woman += 1
        woman.append(element["name"])
    else:
        count_man += 1
        man.append(element["name"])
    if element["age"] >= 20:
        more_than_20.append(element["name"])
    if element["facultet"] == "math":
        math.append(element["name"])
print("Woman: " + ', '.join(woman), 
      "Man: " + ', '.join(man), 
      "The number of women: " + str(count_woman), 
      "The number of man: " + str(count_man),
       "More than 20: " + ', '.join(more_than_20), 
       "In the math: " + ', '.join(math), sep= '\n')
    

# 2) Факториал числа                             
# Пользователь должен ввести с клавиатуры положительное, целое число **n**                                
# Нужно написать програму, которая будет вычислять факториал(произведение                                 
# всех целых чисел от 1 до n) этого числа.    


try:
    user_number = int(input("Enter you number: "))
    if user_number == '':
        raise Exception ("You didn't enter!")
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    factorial = 1
    for i in range(1, user_number + 1):
        factorial *= i
    print("Factorial:", factorial)


# Не забывайте ставить какие-нибудь проверки "на дуркака"(если                             
# пользователь хочет ввести строку\ничего\пробел)                              
# Вывести полученный результат на экран.                              

# 3) Последовательность фибоначи                              
# Пользователь должен ввести с клавиатуры положительное, целое число **n**                             
# Написать код, который находит n-ое число в последовательности Фибоначчи.                           
# ( Последовательность Фибоначчи начинается с чисел 0 и 1, а каждое                               
# последующее число получается путем сложения двух предыдущих)        
# Не забываем проверки "на дурака"                              
# Вывести полученный результат на экран.                                  


try:
    fibonaci = int(input("Enter number: "))
except ValueError as e:
    print(e)

first_number = 0
second_number = 1
result = first_number + second_number

if fibonaci == 1:
    print(f"Fibonace {fibonaci} number:",0)
else:
    for i in range(fibonaci - 2):
        result = first_number + second_number
        first_number = second_number
        second_number = result
    print(f"Fibonace {fibonaci} number:", second_number)


# 4) Вёдра                                
# Есть два ведра:                                          
# Ведро на 3 литра                            
# Ведро на 5 литров                    
# Есть неограниченный запас воды                         
# Необходимо при помощи этих вёдер отмерить ровно четыре литра воды                               
# Можно:                          
# 1) Наливать воду в вёдра                       
# 2) Выливать воду из вёдер                              
# 3) Переливать воду из одного ведра в другое                            
# Нельзя:                        
# Выливать воду частично                              
# Переливать воду частично                            
# В пятилитровое "сразу" налить 4 литра воды. 


bucket_3 = 0   
bucket_5 = 0 
print(
"""Enter comand: 
1 - pour into 3l bucket,
2 - pour into 5l bucket, 
3 - pour it into 3l backet,
4 - pour it into 5l backet,
5 - transfer water from 5l bucket to 3l bucket,
6 - trancfer water from 3l bucket to 5l bucket: """) 
while bucket_5 != 4:
    user_comand = input()  
    match user_comand:
        case "1":
            bucket_3 = 3
            print(f'3l bucket - {bucket_3} liters, 5l bucket - {bucket_5} liters')
        case "2":
            bucket_5 = 5
            print(f'3l bucket - {bucket_3} liters, 5l bucket - {bucket_5} liters')
        case "3":
            bucket_3 = 0
            print(f'3l bucket - {bucket_3} liters, 5l bucket - {bucket_5} liters')
        case "4":
            bucket_5 = 0
            print(f'3l bucket - {bucket_3} liters, 5l bucket - {bucket_5} liters')
        case "5":
            if bucket_5 + bucket_3 < 8:
                while bucket_5 != 0 and bucket_3 != 3:
                    bucket_5 -= 1
                    bucket_3 += 1
                print(f'3l bucket - {bucket_3} liters, 5l bucket - {bucket_5} liters')
            else:
                print('Condredics')
        case "6":
            if bucket_5 + bucket_3 < 8:
                while bucket_5 != 5 and bucket_3 != 0:
                    bucket_3 -= 1
                    bucket_5 += 1
                print(f'bucket 1 - {bucket_3} liters, bucket - {bucket_5} liters')
            else: print('Condredics')
        case _:
            print("These is no such command.")
print("YOU WIN 5l bucet -", bucket_5)


# 1. наливаем в 3(3 ведро - 3, 5 ведро - 0) 1. наливаем в 5 (3 ведро - 0, 5 ведро - 5)
# 2. вливаем в 5 (3 ведро - 0, 5 ведро - 3) 2. выливаем в 3 (3 ведро - 3, 5 ведро - 2)
# 3. наливаем 3 (3 ведро - 3, 5 ведро - 3)  3. выливаем из 3 (3 ведро - 0, 5 ведро - 2)
# 4. вливаем в 5 (3 ведро - 1, 5 ведро - 5) 4. выливаем в 3 (3 ведро - 2, 5 ведро - 0)
# 5. выливаем 5 (3 ведро - 1, 5 ведро - 0)  5. наливаем в 5 (3 ведро - 2, 5 ведро - 5)
# 6. вливаем в 5 (3 ведро - 0, 5 ведро - 1) 6. выливаем в 3 (3 ведро - 3, 5 ведро - 4)    
# 7. вливаем в 3 (3 ведро - 3, 5 ведро - 1) 
# 8. вливаем в 5 (3 ведро - 0, 5 ведро - 4)         
#         