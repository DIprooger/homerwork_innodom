# Задача
# Спроектировать и реализовать класс:
# 🔹 минимум 4 метода;
# 🔹 минимум 2 статических свойства;
# 🔹 минимум 2 динамических свойства

class MyClass:
    text_1 = "Class created:"
    text_2 = "Performing the operation"

    def __init__(self, number_3, number_4):
        print(self.text_1, self.__class__.__name__)
        self.number_3 = number_3
        self.number_4 = number_4

    def __len__(self):
        print(self.text_2, "len: ", end='')
        return len([self.number_3, self.number_4])

    def __add__(self, other):
        print(self.text_2, "+: ", end='')
        return self.number_3 + other.number_3, self.number_4 + other.number_4

    def __gt__(self, other):
        print(self.text_2, ">: ", end='')
        return (self.number_3, self.number_4) > (other.number_3, other.number_4)


my_class = MyClass(5, 6)
my_class_1 = MyClass(3, 4)
print(len(my_class))
print(my_class + my_class_1)
print(my_class > my_class_1)
