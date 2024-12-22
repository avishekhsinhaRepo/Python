class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("{} speak WOFF!!".format(self.name))


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("{} speak Meow!!".format(self.name))



cat = Cat('Felix')
dog = Dog('Fred')

for pet in [cat, dog]:
    pet.speak();