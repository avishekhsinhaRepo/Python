from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def num_of_legs(self):
        pass


class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def num_of_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_of_legs(self):
        return 2


dog = Dog('Tommy')
monkey = Monkey('George')


for animal in [dog, monkey]:
    print(f"Is Instance of Animal : {isinstance(animal, Animal)}")
    print(f'{animal.name} has {animal.num_of_legs()} legs')