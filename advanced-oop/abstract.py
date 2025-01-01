from abc import ABC, abstractmethod


class Animal(ABC):
    def hungry(self):
        print('I want to eat {}!'.format(self.get_favourite_food()))

    @abstractmethod
    def get_favourite_food(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def get_favourite_food(self):
        return 'ribs'


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def get_favourite_food(self):
        return 'milk'


cat = Cat('Tom')
dog = Dog('Tommy')

for animal in [cat, dog]:
    animal.hungry()
