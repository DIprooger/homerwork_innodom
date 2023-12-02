# Поля класса, который вы создали в домашнем задании,
# представьте в виде структуры через класс и с помощью collections.
import collections


class MyClass:
    text_1 = "Class created:"
    text_2 = "Performing the operation"

    def __init__(self, number_1, number_2):
        print(self.text_1, self.__class__.__name__)
        self.number_1 = number_1
        self.number_2 = number_2

    def __len__(self):
        print(self.text_2, "len: ", end='')
        return len([self.number_1, self.number_2])

    def __add__(self, other):
        print(self.text_2, "+: ", end='')
        return self.number_1 + other.number_1, self.number_2 + other.number_2

    def __gt__(self, other):
        print(self.text_2, ">: ", end='')
        return (self.number_1, self.number_2) > (other.number_1, other.number_2)


MyClass = collections.namedtuple('MyClass', ['number_1', 'number_2'])
my_class = MyClass(5, 6)
my_class_1 = MyClass(3, 4)
print(len(my_class))
print(my_class + my_class_1)
print(my_class > my_class_1)
