import csv
import time
import os
import re


class Users():
    id = 0
    role = None
    deleted_at = None
    rating = 0
    user_authorization = {}
    user_email = ''

    def __init__(self):
        if os.path.exists("users.csv"):
            print("The file users.csv is ready for reading and writing.")
            print("Create user.")
        else:
            with open("users.csv", "w") as user:
                field_name = ["ID",
                              "Name",
                              "Last_name",
                              "Mobile_number",
                              "Email",
                              "Password",
                              "Repeat_password",
                              "Created_at",
                              "Updated_at",
                              "Role",
                              "Deleted_at",
                              "Rating"
                              ]

                writer = csv.DictWriter(user, fieldnames=field_name)
                writer.writeheader()
            print("The file users.csv is ready for reading and writing.")

    def email(self):
        if self.id == 0:
            print("Admin Authorization.")
            flag = True
            while flag:
                email = input("Enter you email: ")
                if len(email) > 0:
                    self.user_email = email
                    self.role = "Admin"
                    return True
                else:
                    print("You did not enter your email")

        else:
            with open("users.csv", "r") as user:
                read = csv.DictReader(user)
                flag = True
                while flag:
                    email = input("Enter you email: ")
                    for element in read:
                        if element['Email'] == email:
                            print(f"Welcome {element['Name']}")
                            return False
                        elif len(email) == 0:
                            print("You did not enter your email")
                        else:
                            print("You are not in the system. We begin authorization.")
                            self.user_email = email
                            self.role = "Users"
                            flag = False
                            return True

    def name(self):
        flag = True
        while flag:
            name = input("Enter you name: ")
            last_name = input("Enter you last name: ")
            if name.isalpha() and last_name.isalpha():
                if len(name) > 0 and len(last_name) > 0:
                    self.user_authorization["ID"] = self.id
                    self.user_authorization["Name"] = name
                    self.user_authorization["Last_name"] = last_name
                    self.user_authorization["Email"] = self.user_email
                    self.user_authorization["Role"] = self.role
                    print("The name is correct. Name recorded")
                    print(self.user_authorization)
                    flag = False
                else:
                    print("You did not your name!")
            else:
                print("The name must contain only letters!")

    def mobile_number(self):
        flag = True
        while flag:
            number = input("Enter your mobile number: ")
            if number.isnumeric():
                if len(number) >= 4:
                    self.user_authorization["Mobile_number"] = number
                    print(self.user_authorization)
                    flag = False
                else:
                    print("Your number is short.")
            else:
                print("Your number must consist only of numbers.")

    def password(self):
        is_alnum_reg = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)"
        symbol_reg = r"[!@#$%^&*?_|<>{}]"
        flag = True
        while flag:
            __password = input("Enter your password: ")
            if len(__password) >= 8:
                if re.match(is_alnum_reg, __password):
                    if re.findall(symbol_reg, __password):
                        print("Password is valid.")
                        self.user_authorization["Password"] = __password[::-1]
                        print(self.user_authorization)
                        flag = False
                    else:
                        print("Password isn't valid. the password does not contain special characters.")
                else:
                    print("Password isn't valid. There are no Latin uppercase or lowercase letters in the password")
                    print("and/or there are no number.")
            elif len(__password) > 20:
                print("Password isn't valid. The password is longer than 20 characters.")
            else:
                print("Password isn't valid. The password is shorter than 8 characters.")

    def repeat_password(self):
        flag = True
        while flag:
            repeat = input("Please repeat password: ")
            if self.user_authorization["Password"] == repeat[::-1]:
                print("The passwords matches.")
                self.user_authorization["Repeat_password"] = repeat[::-1]
                self.user_authorization["Created_at"] = time.asctime()
                self.user_authorization["Updated_at"] = time.asctime()
                self.user_authorization["Deleted_at"] = None
                self.user_authorization["Rating"] = 0
                print(self.user_authorization)
                flag = False
            else:
                print("The passwords did not match.")

    def write_users(self):
        with open("users.csv", "a") as user:
            field_name = ["ID",
                          "Name",
                          "Last_name",
                          "Mobile_number",
                          "Email",
                          "Password",
                          "Repeat_password",
                          "Created_at",
                          "Updated_at",
                          "Role",
                          "Deleted_at",
                          "Rating"
                          ]
            writer = csv.DictWriter(user, field_name)
            writer.writerow(self.user_authorization)
            print("User created")
        Users.id += 1


def create_users():
    user = Users()
    exit = ''
    while exit != "no":
        print(f"Create users {user.id}")
        flag = user.email()
        if flag:
            user.name()
            user.mobile_number()
            user.password()
            user.repeat_password()
            user.write_users()
        exit = input("Create users yes or no: ")
    print("User creation is complete.")


class Entry:
    email = None

    def email_user(self):
        email = input("Enter your email: ")
        if os.path.exists("users.csv"):
            with open("users.csv", "r") as users:
                reader = csv.DictReader(users)
                for element in reader:
                    if element["Email"] == email:
                        print(f"Welcom {element['Name']}")
                        self.email = element["Email"]
                        return True, element["Email"]
                else:
                    print("Users not found.")
                    print("To log in, create a user.")
                    return None, None
        else:
            print("To log in, create a user.")
            return None, None

    def password_user(self, email):
        while True:
            password = input("Enter your password: ")
            with open("users.csv", "r") as users:
                reader = csv.DictReader(users)
                for element in reader:
                    if element["Password"] == password[::-1] and element["Email"] == email:
                        print(f"{element['Name']}, You entry in system.")
                        return element['Email']
                else:
                    print("Password not correct.")
                    print("Please repeat your password.")


def entry_users():
    entry = Entry()
    flag, email = entry.email_user()
    if flag:
        email = entry.password_user(email)
        return email


class News:
    id_news = 0
    id_user = None
    email = None
    role = None

    def __init__(self, email):
        self.email = email
        if os.path.exists("news.csv"):
            print("The file news.csv is ready for reading and writing.")
        else:
            with open("news.csv", "w") as user:
                field_name = ["ID",
                              "Header",
                              "Body",
                              "ID_users",
                              "Created_at",
                              "Updated_at",
                              "Deleted_at",
                              "Rating",
                              "Status"
                              ]
                writer = csv.DictWriter(user, fieldnames=field_name)
                writer.writeheader()
            print("The file news.csv is ready for reading and writing.")

    def role(self):
        with open("users.csv", "r") as users:
            read = csv.DictReader(users)
            for element in read:
                if self.email == element["Email"]:
                    self.role = element["Role"]
                    self.id_user = element["ID"]

    def reade_news(self):
        with open("news.csv", "r") as news:
            read = csv.DictReader(news)
            for element in read:
                if element["Deleted_at"] == '' and element["Status"] == 'approved':
                    print(element["ID"])
                    print(element["Header"])
                    print(element["Body"])
                    if element["Rating"] == None:
                        rating = [int(i) for i in element["Rating"].split()]
                        print("Reting:", sum(rating) / (len(rating)))
                    else:
                        print("News not rated.")

    def create_news(self):
        user_create_news = {}
        with open("news.csv", "a") as user:
            field_name = ["ID",
                          "Header",
                          "Body",
                          "ID_users",
                          "Created_at",
                          "Updated_at",
                          "Deleted_at",
                          "Rating",
                          "Status"
                          ]
            writer = csv.DictWriter(user, fieldnames=field_name)
            user_create_news["ID"] = self.id_news
            flag = True
            while flag:
                header = input("Enter name news: ")
                user_create_news["Header"] = header
                if len(header) > 0:
                    flag = False
            flag = True
            while flag:
                body = input("Enter text news: ")
                user_create_news["Body"] = body
                if len(body) > 0:
                    flag = False
            user_create_news["ID_users"] = self.id_user
            user_create_news["Created_at"] = time.asctime()
            user_create_news["Updated_at"] = time.asctime()
            user_create_news["Deleted_at"] = None
            user_create_news["Rating"] = None
            user_create_news["Status"] = "not approved"
            writer.writerow(user_create_news)
        print("News create.")
        News.id_news += 1

    def edit_news(self):
        with open("news.csv", "r") as news:
            read = csv.DictReader(news)
            for element in read:
                if element["ID_users"] == self.id_user and element["Deleted_at"] == '':
                    print(element["ID"])
                    print(element["Header"])
                    print(element["Body"])
                    if element["Rating"] == None:
                        rating = [int(i) for i in element["Rating"].split()]
                        print("Reting:", sum(rating) / (len(rating)))
                    else:
                        print("News not rated.")

        with open("news.csv", "r") as news:
            users_find = input("Enter news id to edit: ")
            new_news = []
            edit_news = {}
            read = csv.DictReader(news)
            for element in read:
                if element["ID"] == users_find:
                    edit_news["ID"] = element["ID"]
                    flag = True
                    while flag:
                        header = input("Enter name news: ")
                        edit_news["Header"] = header
                        if len(header) > 0:
                            flag = False
                    flag = True
                    while flag:
                        body = input("Enter text news: ")
                        edit_news["Body"] = body
                        if len(body) > 0:
                            flag = False
                    edit_news["ID_users"] = element["ID_users"]
                    edit_news["Created_at"] = element["Created_at"]
                    edit_news["Updated_at"] = time.asctime()
                    edit_news["Deleted_at"] = None
                    edit_news["Rating"] = element["Rating"]
                    edit_news["Status"] = element["Status"]
                    print(edit_news)
                    new_news.append(edit_news)
                else:
                    new_news.append(element)
        with open("news.csv", "w") as user:
            field_name = ["ID",
                          "Header",
                          "Body",
                          "ID_users",
                          "Created_at",
                          "Updated_at",
                          "Deleted_at",
                          "Rating",
                          "Status"
                          ]
            writer = csv.DictWriter(user, fieldnames=field_name)
            writer.writeheader()
            for element in new_news:
                writer.writerow(element)
        print("News edit.")

    def rating_news(self):
        with open("news.csv", "r") as news:
            read = csv.DictReader(news)
            for element in read:
                if element["Deleted_at"] == '':
                    print(element["ID"])
                    print(element["Header"])
                    print(element["Body"])
                    if element["Rating"] == None:
                        rating = [int(i) for i in element["Rating"].split()]
                        print("Reting:", sum(rating) / (len(rating)))
                    else:
                        print("News not rated.")
            users_find = input("Enter news id to rating: ")
            edit_news = {}
            new_news = []

        with open("news.csv", "r") as news:
            read = csv.DictReader(news)
            for element in read:
                if element["ID"] == users_find:
                    edit_news["ID"] = element["ID"]
                    edit_news["Header"] = element["Header"]
                    edit_news["Body"] = element["Body"]
                    edit_news["ID_users"] = element["ID_users"]
                    edit_news["Created_at"] = element["Created_at"]
                    edit_news["Updated_at"] = element["Updated_at"]
                    edit_news["Deleted_at"] = None
                    element_rating = None
                    while not(element_rating):
                        rating = input("Enter reiting: ")
                        if rating.isnumeric():
                            element_rating = element["Rating"] + " " + rating
                            edit_news["Rating"] = element_rating
                    print(f"Rating news:{edit_news['Rating']}")
                    edit_news["Status"] = element["Status"]
                    new_news.append(edit_news)
                else:
                    new_news.append(element)
        with open("news.csv", "w") as user:
            field_name = ["ID",
                          "Header",
                          "Body",
                          "ID_users",
                          "Created_at",
                          "Updated_at",
                          "Deleted_at",
                          "Rating",
                          "Status"
                          ]
            writer = csv.DictWriter(user, fieldnames=field_name)
            writer.writeheader()
            for element in new_news:
                writer.writerow(element)
        print("News appreciated.")

        new_user = {}
        new_users = []

        with open("news.csv", "r")as news:
            read = csv.DictReader(news)
            for element in read:
                if element["ID"] == users_find:
                    rating_news = element["Rating"]
                    id_user = element["ID_users"]

        with open("users.csv", "r") as users:
            reade = csv.DictReader(users)
            for element in reade:
                if element["ID"] == id_user:
                    new_user["ID"] = element["ID"]
                    new_user["Name"] = element["Name"]
                    new_user["Last_name"] = element["Last_name"]
                    new_user["Email"] = element["Email"]
                    new_user["Mobile_number"] = element["Mobile_number"]
                    new_user["Password"] = element["Password"]
                    new_user["Repeat_password"] = element["Repeat_password"]
                    new_user["Created_at"] = element["Created_at"]
                    new_user["Updated_at"] = element["Updated_at"]
                    new_user["Role"] = element["Role"]
                    new_user["Deleted_at"] = element["Deleted_at"]
                    rating_news = [int(i) for i in rating_news.split()]
                    new_user["Rating"] = round(sum(rating_news) / (len(rating_news)), 2)
                    new_users.append(new_user)
                else:
                    new_users.append(element)

        with open("users.csv", "w") as users:
            field_name = ["ID",
                          "Name",
                          "Last_name",
                          "Mobile_number",
                          "Email",
                          "Password",
                          "Repeat_password",
                          "Created_at",
                          "Updated_at",
                          "Role",
                          "Deleted_at",
                          "Rating"
                          ]

            writer = csv.DictWriter(users, fieldnames=field_name)
            writer.writeheader()
            for element in new_users:
                writer.writerow(element)
        print("User rating updated.")

    def approval_news(self):
        with open("news.csv", "r") as news:
            read = csv.DictReader(news)
            for element in read:
                if element["Status"] == "not approved" and element["Deleted_at"] == '':
                    print(element["ID"])
                    print(element["Header"])
                    print(element["Body"])
                    if element["Rating"] == None:
                        rating = [int(i) for i in element["Rating"].split()]
                        print("Reting:", sum(rating) / (len(rating)))
                    else:
                        print("News not rated.")

        with open("news.csv", "r") as news:
            users_find = input("Enter news id to approved: ")
            new_news = []
            edit_news = {}
            read = csv.DictReader(news)
            for element in read:
                if element["ID"] == users_find:
                    edit_news["ID"] = element["ID"]
                    edit_news["Header"] = element["Header"]
                    edit_news["Body"] = element["Body"]
                    edit_news["ID_users"] = element["ID_users"]
                    edit_news["Created_at"] = element["Created_at"]
                    edit_news["Updated_at"] = time.asctime()
                    edit_news["Deleted_at"] = None
                    edit_news["Rating"] = element["Rating"]
                    edit_news["Status"] = "approved"
                    new_news.append(edit_news)
                else:
                    new_news.append(element)
        with open("news.csv", "w") as user:
            field_name = ["ID",
                          "Header",
                          "Body",
                          "ID_users",
                          "Created_at",
                          "Updated_at",
                          "Deleted_at",
                          "Rating",
                          "Status"
                          ]
            writer = csv.DictWriter(user, fieldnames=field_name)
            writer.writeheader()
            for element in new_news:
                writer.writerow(element)
        print("News approved")

    def delete_news(self):
        with open("news.csv", "r") as news:
            read = csv.DictReader(news)
            for element in read:
                if (element["ID_users"] == self.id_user or self.role == "Moderator" or self.role == "Admin"
                ) and element["Deleted_at"] == '':
                    print(element["ID"])
                    print(element["Header"])
                    print(element["Body"])
                    if element["Rating"] == None:
                        rating = [int(i) for i in element["Rating"].split()]
                        print("Reting:", sum(rating) / (len(rating)))
                    else:
                        print("News not rated.")

            users_find = input("Enter news id to delet: ")
            edit_news = {}
            new_news = []
        with open("news.csv", "r") as news:
            read = csv.DictReader(news)
            for element in read:
                if element["ID"] == users_find:
                    edit_news["ID"] = element["ID"]
                    edit_news["Header"] = element["Header"]
                    edit_news["Body"] = element["Body"]
                    edit_news["ID_users"] = element["ID_users"]
                    edit_news["Created_at"] = element["Created_at"]
                    edit_news["Updated_at"] = element["Updated_at"]
                    edit_news["Deleted_at"] = time.asctime()
                    edit_news["Rating"] = element["Rating"]
                    edit_news["Status"] = element["Status"]
                    new_news.append(edit_news)
                else:
                    new_news.append(element)
        with open("news.csv", "w") as user:
            field_name = ["ID",
                          "Header",
                          "Body",
                          "ID_users",
                          "Created_at",
                          "Updated_at",
                          "Deleted_at",
                          "Rating",
                          "Status"
                          ]
            writer = csv.DictWriter(user, fieldnames=field_name)
            writer.writeheader()
            for element in new_news:
                writer.writerow(element)
        print("News deleted")

    def menu(self):
        print(self.role)
        if self.email:
            match self.role:
                case "Admin":
                    exit = ''
                    while exit != "exit":
                        print("Command: 1.reade, 2.delete, 3.exit")
                        command = input("Enter you command: ")
                        match command:
                            case "reade":
                                self.reade_news()
                            case "delete":
                                self.delete_news()
                            case "exit":
                                exit = "exit"
                            case _:
                                print("Command not found")
                case "Moderator":
                    exit = ''
                    while exit != "exit":
                        print("Command: 1.reade, 2.approval, 3.edit, 4.delete, 5.exit")
                        command = input("Enter you command: ")
                        match command:
                            case "reade":
                                self.reade_news()
                            case "approval":
                                self.approval_news()
                            case "edit":
                                self.edit_news()
                            case "delete":
                                self.delete_news()
                            case "exit":
                                exit = "exit"
                            case _:
                                print("Command not found")
                case "Users":
                    exit = ''
                    while exit != "exit":
                        print("Command: 1.create, 2.edit, 3.delete, 4.rating, 5.exit")
                        command = input("Enter you command: ")
                        match command:
                            case "create":
                                self.create_news()
                            case "edit":
                                self.edit_news()
                            case "delete":
                                self.delete_news()
                            case "rating":
                                self.rating_news()
                            case "exit":
                                exit = "exit"
                            case _:
                                print("Command not found")
        else:
            print("To log in, create a user.")


def news(email):
    user_news = News(email)
    user_news.role()
    user_news.menu()


class Comment:
    id_comment = 0
    id_user = None
    role = None

    def __init__(self, email):
        self.email = email
        if os.path.exists("comment.csv"):
            print("The file news.csv is ready for reading and writing.")
        else:
            with open("comment.csv", "w") as comment:
                field_name = ["ID",
                              "Body",
                              "ID_users",
                              "ID_news",
                              "Created_at",
                              "Updated_at",
                              "Deleted_at"
                              ]
                writer = csv.DictWriter(comment, fieldnames=field_name)
                writer.writeheader()
            print("The file news.csv is ready for reading and writing.")

    def role(self):
        with open("users.csv", "r") as users:
            read = csv.DictReader(users)
            for element in read:
                if self.email == element["Email"]:
                    self.role = element["Role"]
                    self.id_user = element["ID"]

    def reade_comment(self):
        with open("news.csv", "r") as news:
            read = csv.DictReader(news)
            for element in read:
                if element["Deleted_at"] == '':
                    print(element["ID"])
                    print(element["Header"])
                    print(element["Body"])
            mews_comment = input("Enter the id of the news to see comments: ")
        with open("comment.csv", "r") as comment:
            read = csv.DictReader(comment)
            for element in read:
                if element["Deleted_at"] == '' and element["ID_news"] == mews_comment:
                    print(element["ID"])
                    print(element["Body"])

    def create_comment(self):
        with open("news.csv", "r") as news:
            read = csv.DictReader(news)
            for element in read:
                if element["Deleted_at"] == '':
                    print(element["ID"])
                    print(element["Body"])

        id_news = int(input("Enter the ID of the news to which to add a comment: "))
        user_create_comment = {}
        with open("comment.csv", "a") as comment:
            field_name = ["ID",
                          "Body",
                          "ID_users",
                          "ID_news",
                          "Created_at",
                          "Updated_at",
                          "Deleted_at"
                          ]
            writer = csv.DictWriter(comment, fieldnames=field_name)
            user_create_comment["ID"] = self.id_comment
            flag = True
            while flag:
                body = input("Enter comment text: ")
                user_create_comment["Body"] = body
                if len(body) > 0:
                    flag = False
            user_create_comment["ID_users"] = self.id_user
            user_create_comment["ID_news"] = id_news
            user_create_comment["Created_at"] = time.asctime()
            user_create_comment["Updated_at"] = None
            user_create_comment["Deleted_at"] = None
            writer.writerow(user_create_comment)
        print("comment create.")
        Comment.id_comment += 1

    def edit_comment(self):
        with open("comment.csv", "r") as comment:
            read = csv.DictReader(comment)
            for element in read:
                if element["ID_users"] == self.id_user and element["Deleted_at"] == '':
                    print(element["ID"])
                    print(element["Body"])

        with open("comment.csv", "r") as comment:
            users_find = input("Enter news id to edit: ")
            new_comment = []
            edit_comment = {}
            read = csv.DictReader(comment)
            for element in read:
                if element["ID"] == users_find:
                    edit_comment["ID"] = element["ID"]
                    flag = True
                    while flag:
                        body = input("Enter comment text: ")
                        edit_comment["Body"] = body
                        if len(body) > 0:
                            flag = False
                    edit_comment["ID_users"] = element["ID_users"]
                    edit_comment["Created_at"] = element["Created_at"]
                    edit_comment["Updated_at"] = time.asctime()
                    edit_comment["Deleted_at"] = None
                    print(edit_comment)
                    new_comment.append(edit_comment)
                else:
                    new_comment.append(element)
        with open("comment.csv", "w") as comment:
            field_name = ["ID",
                          "Body",
                          "ID_users",
                          "ID_news",
                          "Created_at",
                          "Updated_at",
                          "Deleted_at"
                          ]
            writer = csv.DictWriter(comment, fieldnames=field_name)
            writer.writeheader()
            for element in new_comment:
                writer.writerow(element)
        print("comment edit.")


    def delete_comment(self):
        with open("comment.csv", "r") as comment:
            read = csv.DictReader(comment)
            for element in read:
                if (element["ID_users"] == self.id_user or self.role == "Moderator" or self.role == "Admin"
                ) and element["Deleted_at"] == '':
                    print(element["ID"])
                    print(element["Body"])

            users_find = input("Enter comment id to delete: ")
            edit_comment = {}
            new_comment = []
        with open("comment.csv", "r") as comment:
            read = csv.DictReader(comment)
            for element in read:
                if element["ID"] == users_find:
                    edit_comment["ID"] = element["ID"]
                    edit_comment["Body"] = element["Body"]
                    edit_comment["ID_users"] = element["ID_users"]
                    edit_comment["ID_news"] = element["ID_news"]
                    edit_comment["Created_at"] = element["Created_at"]
                    edit_comment["Updated_at"] = element["Updated_at"]
                    edit_comment["Deleted_at"] = time.asctime()
                    new_comment.append(edit_comment)
                else:
                    new_comment.append(element)
        with open("comment.csv", "w") as comment:
            field_name = ["ID",
                          "Body",
                          "ID_users",
                          "ID_news",
                          "Created_at",
                          "Updated_at",
                          "Deleted_at"
                          ]
            writer = csv.DictWriter(comment, fieldnames=field_name)
            writer.writeheader()
            for element in new_comment:
                writer.writerow(element)
        print("News deleted")


    def menu(self):
        print(self.role)
        if self.email:
            match self.role:
                case "Admin":
                    exit = ''
                    while exit != "exit":
                        print("Command: 1.reade, 2.delete, 3.exit")
                        command = input("Enter you command: ")
                        match command:
                            case "reade":
                                self.reade_comment()
                            case "delete":
                                self.delete_comment()
                            case "exit":
                                exit = "exit"
                            case _:
                                print("Command not found")
                case "Moderator":
                    exit = ''
                    while exit != "exit":
                        print("Command: 1.reade, 2.edit, 3.delete, 4.exit")
                        command = input("Enter you command: ")
                        match command:
                            case "reade":
                                self.reade_comment()
                            case "approval":
                                self.edit_comment()
                            case "delete":
                                self.delete_comment()
                            case "exit":
                                exit = "exit"
                            case _:
                                print("Command not found")
                case "Users":
                    exit = ''
                    while exit != "exit":
                        print("Command: 1.create, 2.edit, 3.delete, 4.exit")
                        command = input("Enter you command: ")
                        match command:
                            case "create":
                                self.create_comment()
                            case "edit":
                                self.edit_comment()
                            case "delete":
                                self.delete_comment()
                            case "exit":
                                exit = "exit"
                            case _:
                                print("Command not found")
        else:
            print("To log in, create a user.")


def comment(email):
    comment = Comment(email)
    comment.role()
    comment.menu()


class Admin:
    role = None

    def __init__(self, email):
        self.email = email
        with open("users.csv", "r") as users:
            read = csv.DictReader(users)
            for element in read:
                if element["Email"] == email:
                    self.role = element["Role"]

    def entry_user(self):
        if self.role == "Admin":
            print("Welcome Admin.")
            return True
        else:
            print("You are not Admin")
            return False

    def create_role(self):
        with open("users.csv", "r") as user:
            reade = csv.DictReader(user)
            for element in reade:
                print(element["ID"])
                print(element["Name"])
                print(element["Last name"])
        moderator = input("Enter your user ID to create a moderator.")
        new_moderator = {}
        new_users = []
        with open("users.csv", "r") as user:
            reade = csv.DictReader(user)
            for element in reade:
                if element["ID"] == moderator and element["Deleted_at"] == '':
                    new_moderator["ID"] = element["ID"]
                    new_moderator["Name"] = element["Name"]
                    new_moderator["Last_name"] = element["Last_name"]
                    new_moderator["Mobile_number"] = element["Mobile_number"]
                    new_moderator["Email"] = element["Email"]
                    new_moderator["Password"] = element["Password"]
                    new_moderator["Repeat_password"] = element["Repeat_password"]
                    new_moderator["Created_at"] = element["Created_at"]
                    new_moderator["Updated_at"] = element["Updated_at"]
                    role = ''
                    while len(role) == 0:
                        print("Role: 1.moderator, 2.user")
                        admin_role_change = input("Enter role: ")
                        match admin_role_change:
                            case "moderator":
                                role = "Moderator"
                            case "users":
                                role = "Users"
                            case _:
                                print("Role not found.")
                    new_moderator["Role"] = role
                    new_moderator["Deleted_at"] = element["Deleted_at"]
                    new_moderator["Rating"] = element["Rating"]
                    new_users.append(new_moderator)
                else:
                    new_users.append(element)

        with open("users.csv", "w") as user:
            file_name = ["ID",
                          "Name",
                          "Last_name",
                          "Mobile_number",
                          "Email",
                          "Password",
                          "Repeat_password",
                          "Created_at",
                          "Updated_at",
                          "Role",
                          "Deleted_at",
                          "Rating"
                          ]
            write = csv.DictWriter(user, fieldnames=file_name)
            write.writeheader()
            for element in new_users:
                write.writerow(element)
        print("Moderator create.")


    def reade_user(self):
        with open("users.csv", "r") as users:
            reade = csv.DictReader(users)
            for element in reade:
                print(element["ID"])
                print(element["Name"])
                print(element["Last name"])


    def delet_users(self):
        with open("users.csv", "r") as user:
            reade = csv.DictReader(user)
            for element in reade:
                print(element["ID"])
                print(element["Name"])
                print(element["Last name"])
        moderator = input("Enter your user ID to create a moderator.")
        new_moderator = {}
        new_users = []
        with open("users.csv", "r") as user:
            reade = csv.DictReader(user)
            for element in reade:
                if element["ID"] == moderator and element["Deleted_at"] == '':
                    new_moderator["ID"] = element["ID"]
                    new_moderator["Name"] = element["Name"]
                    new_moderator["Last_name"] = element["Last_name"]
                    new_moderator["Mobile_number"] = element["Mobile_number"]
                    new_moderator["Email"] = element["Email"]
                    new_moderator["Password"] = element["Password"]
                    new_moderator["Repeat_password"] = element["Repeat_password"]
                    new_moderator["Created_at"] = element["Created_at"]
                    new_moderator["Updated_at"] = element["Updated_at"]
                    new_moderator["Role"] = element["Role"]
                    new_moderator["Deleted_at"] = time.asctime()
                    new_moderator["Rating"] = element["Rating"]
                    new_users.append(new_moderator)
                else:
                    new_users.append(element)

        with open("users.csv", "w") as user:
            file_name = ["ID",
                         "Name",
                         "Last_name",
                         "Mobile_number",
                         "Email",
                         "Password",
                         "Repeat_password",
                         "Created_at",
                         "Updated_at",
                         "Role",
                         "Deleted_at",
                         "Rating"
                         ]
            write = csv.DictWriter(user, fieldnames=file_name)
            write.writeheader()
            for element in new_users:
                write.writerow(element)
        print("Users delete.")


    def menu(self):
        exit = ''
        while exit != "exit":
            print("Command: 1.read, 2.delete, 3.moderator, 4.exit")
            command = input("Enter command: ")
            match command:
                case "read":
                    self.reade_user()
                case "delete":
                    self.delet_users()
                case "moderator":
                    self.create_role()
                case "exit":
                    exit = "exit"
                case _:
                    print("Command not found.")


def admin_command(email):
    admin = Admin(email)
    flag = admin.entry_user()
    if flag:
        admin.menu()


print("Start.")
exit = ''
while exit != "exit":
    print("Command: 1.create, 2.entry, 3.exit")
    command = input("Enter command: ")
    match command:
        case "create":
            create_users()
        case "entry":
            email = entry_users()
            exit = ''
            if email:
                while exit != "exit":
                    print("Command: 1.news, 2.comments, 3.admin, 4.exit")
                    command = input("Enter command: ")
                    match command:
                        case "news":
                            news(email)
                        case "comments":
                            comment(email)
                        case "admin":
                            admin_command(email)
                        case "exit":
                            exit = "exit"
                        case _:
                            print("Command not found!")
        case "exit":
            exit = "exit"
        case _:
            print("Command not found!")

print("End.")
