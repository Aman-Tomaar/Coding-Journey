# Polymorphism : Greek word meaning "many forms".
#               TWO WAYS TO ACHIEVE POLYMORPHISM
#                  1. Inheritance = An object could be treated of the same type as a parent class
#                  2. "Duck typing" = Object must have necessary attributes/methods


print("Polymorphism using Inheritance")
from abc import ABC, abstractmethod


class shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class pizza(Circle):
    def __init__(self, radius, toppings):
        super().__init__(radius)
        self.toppings = toppings

    def area(self):
        return super().area()

    def get_toppings(self):
        return self.toppings


# Creating objects of the subclasses
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(4, 6),
    Square(5),
    pizza(5, ["pepperoni", "mushrooms"]),
]

# Calling the area method
for shape in shapes:
    print(f"{shape.area()}")
