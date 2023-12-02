# Реализуйте систему обработки заказов в ресторане.
# Можно создать абстрактный класс Dish, который определяет общий интерфейс для всех блюд, и классы Starter, MainCourse и Dessert,
# которые наследуются от Dish и предоставляют конкретную реализацию для каждого типа блюд. Кроме того, можно создать абстрактный класс Order,
# который определяет общий интерфейс для заказов, и классы TableOrder и DeliveryOrder,
# которые наследуются от Order и предоставляют конкретную реализацию для заказов в ресторане и на доставку соответственно.


from abc import ABC, abstractmethod

menu_starter = [{'dish': 'Beef Stroganoff', 'price': 2},
                {'dish': 'Borscht', 'price': 5},
                {'dish': 'Round fried meat pie', 'price': 100},
                {'dish': 'Curd tart	', 'price': 1}
                ]

menu_dessert = [{'dish': 'Pancake', 'price': 23},
                {'dish': 'Preserve', 'price': 0.2},
                {'dish': 'Thick pancake	', 'price': 70},
                {'dish': 'Mues', 'price': 9}
                ]

menu_main_course = [{'dish': 'Deep-fried potatoes	', 'price': 4},
                    {'dish': 'Porridge', 'price': 11},
                    {'dish': 'Cream of rice', 'price': 34},
                    {'dish': 'Lecho', 'price': 14}
                    ]


class Dish(ABC):
    @abstractmethod
    def reade_nemu(self):
        pass

    @abstractmethod
    def take_dish(self):
        pass


class WorkWhichMenu(Dish):
    price = 0

    def __init__(self, name_user, menu):
        self.name_user = name_user
        self.menu = menu
        self.user_order = []


    def reade_nemu(self):
        for element in self.menu:
            print(element)

    def take_dish(self):
        user_choice = input("Enter your choice: ")
        for element in self.menu:
            if element['dish'] == user_choice:
                self.user_order.append(element)
                self.price += int(element['price'])
        print(f"Your order {self.name_user}: ")
        print(self.user_order)
        print('Price:', self.price)
        return self.user_order


class Starter(WorkWhichMenu):

    def __init__(self, name_user, menu):
        super().__init__(name_user, menu)

    def reade_nemu(self):
        print('Menu Starter: ')
        super().reade_nemu()

    def take_dish(self):
        order = super().take_dish()
        return order


class MainCourse(WorkWhichMenu):
    def __init__(self, name_user, menu):
        super().__init__(name_user, menu)

    def reade_nemu(self):
        print('Menu Main Course: ')
        super().reade_nemu()

    def take_dish(self):
        order = super().take_dish()
        return order


class Dessert(WorkWhichMenu):
    def __init__(self, name_user, menu):
        super().__init__(name_user, menu)

    def reade_nemu(self):
        print('Menu Dessert: ')
        super().reade_nemu()

    def take_dish(self):
        order = super().take_dish()
        return order


class Order(ABC):

    @abstractmethod
    def order(self):
        pass


class TableOrder(Order):

    def __init__(self, user_name):
        self.user_name = user_name
        self.table = [1, 2, 3, 4, 5]
        self.choice = ''

    def order(self):
        print(self.table)
        self.choice = input("Enter numbet the table: ")
        self.table.pop(int(self.choice) - 1)
        print(f'You order table {name_user}.')


class DeliveryOrder(Order):

    def __init__(self, name_user, menu_starter, menu_dessert, menu_main_course):
        self.name_user = name_user
        self.menu_starter = menu_starter
        self.menu_dessert = menu_dessert
        self.menu_main_course = menu_main_course
        self.command = 'Start'
        self.user_order = []
        self.adress = ''

    def order(self):
        while self.command:
            print("Press enter to exit")
            self.command = input("Enter your command: ")
            match self.command:
                case 'starter':
                    starter = Starter(self.name_user, self.menu_starter)
                    starter.reade_nemu()
                    self.user_order.append(starter.take_dish())
                case 'course':
                    main_course = MainCourse(self.name_user, self.menu_dessert)
                    main_course.reade_nemu()
                    self.user_order.append(main_course.take_dish())
                case 'desert':
                    desert = Dessert(self.name_user, self.menu_main_course)
                    desert.reade_nemu()
                    self.user_order.append(desert.take_dish())
        print(self.user_order)
    def order_adres(self):
        self.adress = input("Enter your adress: ")
        return self.adress


name_user = input("Enter your name: ")
delivery_order = DeliveryOrder(name_user, menu_starter, menu_main_course, menu_dessert)
delivery_order.order()
delivery_order.order_adres()
table = TableOrder(name_user)
table.order()


