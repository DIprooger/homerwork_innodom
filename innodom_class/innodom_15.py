# 🔹 Добавьте магические методы __getitem__ и __setitem__ в ваш реализованный класс.
# 🔹 Добавьте один статический и один классовый метод к вашему классу.
import statistics


class MyClass:
    text_1 = "Class created:"
    text_2 = "Performing the operation"
    number_dict = {}

    @staticmethod
    def hello(name):
        print(f"Helo {name}, let's start work")

    @classmethod
    def variables(cls):
        print(f"You work in class: {cls.__name__}")

    def __init__(self, number_3, number_4):
        print(self.text_1, self.__class__.__name__)
        self.number_3 = number_3
        self.number_4 = number_4
        # self.numbers = [self.number_3, self.number_4]
        self.numbers = {0: self.number_3, 1: self.number_4}

    def __len__(self):
        print(self.text_2, "len: ", end='')
        return len([self.number_3, self.number_4])

    def __add__(self, other):
        print(self.text_2, "+: ", end='')
        return self.number_3 + other.number_3, self.number_4 + other.number_4

    def __gt__(self, other):
        print(self.text_2, ">: ", end='')
        return (self.number_3, self.number_4) > (other.number_3, other.number_4)

    def __setitem__(self, key, value):
        self.numbers[key] = value

    def __getitem__(self, item):
        return self.numbers[item]


name = input("Enter your name: ")
my_class = MyClass(5, 6)
my_class_1 = MyClass(3, 4)
my_class.hello(name)
my_class.variables()
print(len(my_class))
print(my_class + my_class_1)
print(my_class > my_class_1)
print(f"In the object my_class at index 0 there is an element: {my_class[0]}")
my_class[0] = 10
print(f"In the object my_class at index 0 there is an element: {my_class[0]}")
