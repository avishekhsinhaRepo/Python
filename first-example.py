class Car():
    def __init__(self, color, make):
        self.color = color;
        self.make = make;
    def startEngine(self):
        print("Time to start the {} which is {} in color".format(self.make,self.color))



class EVCar(Car):
    def __init__(self, color, make, batteryCapacity):
        super().__init__(color,make)
        self.batteryCapacity = batteryCapacity;

honda = Car('blue', "city");
toyota = Car(make='Corolla',color="white")
tesla= EVCar("grey","Model S", 75)

honda.startEngine()
toyota.startEngine()
tesla.startEngine()

