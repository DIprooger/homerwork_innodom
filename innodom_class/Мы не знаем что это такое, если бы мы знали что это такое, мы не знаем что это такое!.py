import csv
import time
import re
import os


class Users():
    id = 0
    user_authorization = {}
    user_email = ''

    def __init__(self):
        if os.path.exists("users.csv"):
            print("The file users.csv is ready for reading and writing.")
        else:
            with open("users.csv", "w") as user:
                field_name = ['ID',
                              'Имя',
                              'Фамилия',
                              'Телефон',
                              'Email',
                              'Пароль',
                              'Повтор пароля',
                              'Дата создания',
                              'Дата обновления',
                              'Роль',
                              'Дата удаления',
                              'Рейтинг'
                            ]
                writer = csv.DictWriter(user, fieldnames=field_name)
                writer.writeheader()
            print("The file users.csv is ready for reading and writing.")

    def email(self, email):
        with open("users.csv", "r") as user:
            read = csv.DictReader(user)
            for element in read:
                if element['Email'] == email:
                    print(f"Welcome {element['Имя']}")
                    return False
                elif len(email) == 0 or email == None:
                    print("You did not enter your email")
                    return True
                else:
                    print("You are not in the system. We begin authorization.")
                    self.user_email = email
                    return False

    def name(self, name):
        if name.isalpha() and len(name) > 0:
            self.user_authorization['Имя'] = name
            self.user_authorization['Email'] = self.user_email
            print("The name is correct. Name recorded")
            # print(self.user_authorization)
            return False
        elif len(name) == 0:
            print("You did not your name!")
            return True
        else:
            print("The name must contain only letters!")
            return True

    def password(self, password):
        is_alnum_reg = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)"
        symbol_reg = r"[!@#$%^&*?_|<>{}]"
        if len(password) >= 8:
            if re.match(is_alnum_reg, password):
                if re.findall(symbol_reg, password):
                    print("Password is valid.")
                    self.user_authorization['Пароль'] = password
                    # print(self.user_authorization)
                    return False
                else:
                    print("Password isn't valid. the password does not contain special characters.")
                    return True
            else:
                print("Password isn't valid. There are no Latin uppercase or lowercase letters in the password")
                print("and/or there are no number.")
                return True
        elif len(password) > 20:
            print("Password isn't valid. The password is longer than 20 characters.")
            return True
        else:
            print("Password isn't valid. The password is shorter than 8 characters.")
            return True

    def repeat_password(self, repeat):
        if self.user_authorization['Пароль'] == repeat:
            print("The passwords matches.")
            self.user_authorization['Повтор пароля'] = repeat
            # print(self.user_authorization)
            return False
        else:
            print("The passwords did not match.")
            return True

    def write_users(self):
        with open("users.csv", "a") as user:
            field_name = ['ID',
                          'Имя',
                          'Фамилия',
                          'Телефон',
                          'Email',
                          'Пароль',
                          'Повтор пароля',
                          'Дата создания',
                          'Дата обновления',
                          'Роль',
                          'Дата удаления',
                          'Рейтинг'
                          ]
            writer = csv.DictWriter(user, fieldnames=field_name)
            writer.writeheader()
            writer.writerow(self.user_authorization)
            print("User created")
            return False



#     def __init__(self, **kwargs):
#         self.password = None
#         self.kwargs = kwargs
#
#     @classmethod
#     def write_admin(cls):
#         cls.information_admin = {
#             'ID': 1,
#             'Имя': input("Enter your name: "),
#             'Фамилия': input("Enter last name: "),
#             'Телефон': input("Enter your mobile number: "),
#             'Email': input("Enter your email: "),
#             'Пароль': cls.wriete_password(user),
#             'Повтор пароля': cls.repeat_password(user),
#             'Дата создания': time.asctime(),
#             'Дата обновления': time.asctime(),
#             'Роль': "Admin",
#             'Дата удаления': None,
#             'Рейтинг': 0
#         }
#         return cls.information_admin
#
#     def wriete_password(self):
#         flag = True
#         while flag:
#             user_password = input("Enter your pasword: ")
#             flag = self.corect_password(user_password)
#         return user_password
#
#     def corect_password(self, user_password):
#         self.password = user_password
#         is_alnum_reg = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)"
#         symbol_reg = r"[!@#$%^&*?_|<>{}]"
#         if len(self.password) >= 8:
#             if re.match(is_alnum_reg, self.password):
#                 if re.findall(symbol_reg, self.password):
#                     print("Password is valid.")
#                     return False
#                 else:
#                     print("Password isn't valid. the password does not contain special characters.")
#                     return True
#             else:
#                 print("Password isn't valid. There are no Latin uppercase or lowercase letters in the password")
#                 print("and/or there are no number.")
#                 return True
#         elif len(self.password) > 20:
#             print("Password isn't valid. The password is longer than 20 characters.")
#             return True
#         else:
#             print("Password isn't valid. The password is shorter than 8 characters.")
#             return True
#
#     def repeat_password(self):
#         flag = True
#         while flag:
#             repeat = input("Please repeat password: ")
#             print(self.password)
#             if self.password == repeat:
#                 return repeat
#
#     def write_table_admin(self):
#         with open("users.csv", "w") as write_users:
#             fieldnames = ['ID',
#                           'Имя',
#                           'Фамилия',
#                           'Телефон',
#                           'Email',
#                           'Пароль',
#                           'Повтор пароля',
#                           'Дата создания',
#                           'Дата обновления',
#                           'Роль',
#                           'Дата удаления',
#                           'Рейтинг'
#                           ]
#             writer = csv.DictWriter(write_users, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerow(self.write_admin())
#
#
# print("Creating an admin")
# user = Users()
# user.write_table_admin()

