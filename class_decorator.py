def add_perimeter(cls):
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    cls.calculate_perimeter = calculate_perimeter
    return cls
@add_perimeter
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
