# Задача 1
# Создайте класс Person с приватным атрибутом __name и публичным методом get_name(), который возвращает имя объекта.
# Затем создайте объект этого класса и вызовите метод get_name() для получения имени объекта.


class Person:

    def __init__(self):
        self.__name = "Hello"

    def get_name(self):
        return self.__name

person = Person()
print(person.get_name())


# Задача 2
# Унаследуйте от класса Animal класс Cat, Dog, Hamster. Продумайте и реализуйте их логику.


class Animal:
    def __init__(self):
        self.paws = 4
        self.tail = True
        self.ears = 2
        self.wool = True


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def say_new(self):
        print(f"Your {self.name} say 'Mew'!")

    def __str__(self):
        return f"""
        Cat's name: {self.name}
        Cat's age: {self.age}
        Cat's paws: {self.paws}
        Cat with tail? - {self.tail}
        Cat's ears: {self.ears}
        Cat have wool? - {self.wool}
    """

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def say_new(self):
        print(f"Your {self.name} say 'Woof'!")

    def __str__(self):
        return f"""
        Dog's name: {self.name}
        Dog's age: {self.age}
        Dog's paws: {self.paws}
        Dog with tail? - {self.tail}
        Dog's ears: {self.ears}
        Dog have wool? - {self.wool}
    """

class Hamster(Animal):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def say_new(self):
        print(f"Your {self.name} say 'Pew'!")

    def __str__(self):
        return f"""
        Hamster's name: {self.name}
        Hamster's age: {self.age}
        Hamster's paws: {self.paws}
        Hamster with tail? - {self.tail}
        Hamster's ears: {self.ears}
        Hamster have wool? - {self.wool}
    """

cat = Cat(input("Enter name: "), input("Enter age: "))
dog = Dog(input("Enter name: "), input("Enter age: "))
hamster = Hamster(input("Enter name: "), input("Enter age: "))

print(cat)
print(cat.say_new())
print(dog)
print(dog.say_new())
print(hamster)
print(hamster.say_new())