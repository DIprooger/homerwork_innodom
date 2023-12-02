import os
import csv
import re

# with open("users.csv", "w") as user:
#     field_name = ["name", "email", "password", "repeat password"]
#
#     writer = csv.DictWriter(user, fieldnames=field_name)
#     writer.writeheader()
#
#     writer.writerow({"name": "Diana", "email": "dfprivet@gmail.com", "password": "Dd$485720vnjdv",
#                      "repeat password": "Dd$485720vnjdv"})
#     writer.writerow(
#         {"name": "Pacha", "email": "pacha@gmail.com", "password": "Dd$485720pach", "repeat password": "Dd$485720pach"})
#     writer.writerow(
#         {"name": "Meg", "email": "meg@gmail.com", "password": "Mm#$334dfe", "repeat password": "Mm#$334dfe"})


class Entry:
    user_authorization = {}
    user_email = ''

    def __init__(self):
        if os.path.exists("users.csv"):
            print("The file users.csv is ready for reading and writing.")
        else:
            with open("users.csv", "w") as user:
                field_name = ["name", "email", "password", "repeat password"]

                writer = csv.DictWriter(user, fieldnames=field_name)
                writer.writeheader()
            print("The file users.csv is ready for reading and writing.")

    def email(self, email):
        with open("users.csv", "r") as user:
            read = csv.DictReader(user)
            for element in read:
                if element["email"] == email:
                    print(f"Welcome {element['name']}")
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
            self.user_authorization["name"] = name
            self.user_authorization["email"] = self.user_email
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
                    self.user_authorization["password"] = password
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
        if self.user_authorization["password"] == repeat:
            print("The passwords matches.")
            self.user_authorization["repeat password"] = repeat
            # print(self.user_authorization)
            return False
        else:
            print("The passwords did not match.")
            return True

    def write_users(self):
        with open("users.csv", "a") as user:
            field_name = ["name", "email", "password", "repeat password"]
            writer = csv.DictWriter(user, field_name)
            # writer.writeheader()
            # writer = csv.writer(user)
            writer.writerow(self.user_authorization)
            print("User created")
            return False


print("Press 'q' to exit")
command = ''
flag = True
flag_user = True

while command != "q" and flag:
    user = Entry()
    # while not command:
    #     command = input("Enter your email: ")

    if command == 'q':
        break

    while flag:
        command = input("Enter your email: ")
        flag = user.email(command)

    # flag = True
    if not(flag):
        while flag_user:
            command = input("Enter your name: ")
            if command == 'q':
                break
            flag_user = user.name(command)
        flag_user = True

        if command == 'q':
            break

        while flag_user:
            command = input("Enter password: ")
            if command == 'q':
                break
            flag_user = user.password(command)
        flag_user = True

        if command == 'q':
            break

        while flag_user:
            command = input("Please repeat your password: ")
            if command == 'q':
                break
            flag_user = user.repeat_password(command)
        flag_user = True

        if command == 'q':
            break
        flag = user.write_users()

print("end")
