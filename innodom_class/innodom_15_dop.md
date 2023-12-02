>Попробуйте реализовать техническое задание для любой своей ранее выполненной программы:<br/>
🔹 опишите требования к программе (какие функции программа должна выполнять, кому эта программа подходит)<br/>
🔹 проведите ручное тестирование вашей программы, попробуйте проверить программу разными значениями и <br/>
сделайте таблицу функция, ожидание работы, фактический результат - небольшой тест-кейс<br/>
🔹 описать руководство пользователя
# Technical specifications for the file "entry.py"
## Program functions
1. User availability check
2. If the user is not creating a user
3. Exiting the program by entering a letter "q"

A program where you need to register and check if a user is in the system.
## Testing the program
Testing 1 user input. The user enters his email. If it is in the system, a message will be displayed. 
If not, then the user registers in the system. There is no check for a correctly written email.
```python
command = input("Enter your email: ")
```
For example, a user __Diana__ with an email __dfprivet@gmail.com__ has already been registered.

| input              | expectation              | output           |
|--------------------|--------------------------|------------------|
| tania@gmail.com    | You are not in the system. We begin authorization. | You are not in the system. We begin authorization. |
| q                  | end                      | end              |
| dfprivet@gmail.com | Welcome Diana <br/>  end | Welcome Diana <br/> end |
| None               | You did not enter your email              | You did not enter your email       |
| 4r7                | You are not in the system. We begin authorization.                | You are not in the system. We begin authorization.        |
<br/> 
<br/> 
Testing 2 user input. The user enters his name.

```python
command = input("Enter your name: ")
```

| input | expectation              | output                             |
|-----|--------------------------|------------------------------------|
| Tania | The name is correct. Name recorded | The name is correct. Name recorded |
| q   | end                      | end                                |
| 34  | the name must contain only letters! | the name must contain only letters!|
| None | You did not your name!             | You did not your name!             |
<br/> 
<br/> 
Testing 3 user input. The user enters his password.

```python
command = input("Enter password: ")
```

| input    | expectation                                                                                                        | output                                                                                                             |
|----------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| sd       | Password isn't valid. The password is shorter than 8 characters.                                                   | Password isn't valid. The password is shorter than 8 characters.                                                   |
| hhhhhhhh | Password isn't valid. There are no Latin uppercase or lowercase letters in the password and/or there are no number | Password isn't valid. There are no Latin uppercase or lowercase letters in the password and/or there are no number |
| Aa1aaaaa        | Password isn't valid. the password does not contain special characters.                                            | Password isn't valid. the password does not contain special characters.                                            |
| aA1AAAAaaa@       | Password is valid.                                                                                                 | Password is valid.                                                                                                 |
| q        | end                                                                                                                | end                                                                                                                |
| None     | Password isn't valid. The password is shorter than 8 characters.                                                   | Password isn't valid. The password is shorter than 8 characters.                                                   |
<br/> 
<br/> 
Testing 4 user input. The user repeat his password.

```python
command = input("Please repeat your password: ")
```

| input    | expectation                     | output                      |
|----------|---------------------------------|-----------------------------|
| a      | The passwords did not match.    | The passwords did not match |
| aA1AAAAaaa@       | The passwords matches.  <br/>  User created<br/> end | The passwords matches. <br/> User created<br/>end        |
| q        | end                             | end                         |
| None     | The passwords did not match.    | The passwords did not match. |


## User guide

Write what the program asks and read carefully what it outputs