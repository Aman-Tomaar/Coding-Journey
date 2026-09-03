#


class shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled


class circle(shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def disc(self):
        print(
            f"Color of Circle is {self.color}, It is {'filled' if self.is_filled == True else 'NOT filled'}"
        )

    def Circumference(self):
        print(f"Circumference of Circle is {2 * 3.14 * self.radius}")


class square(shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side

    def disc(self):
        print(
            f"Color of Square is {self.color}, It is {'filled' if self.is_filled == True else 'NOT filled'}"
        )

    def area(self):
        print(f"Area of Square is {self.side * self.side}")


class triangle(shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def disc(self):
        print(
            f"Color of Triangle is {self.color}, It is {'filled' if self.is_filled == True else 'NOT filled'}"
        )

    def area(self):
        print(f"Area of Triangle is { 0.5 * self.width * self.height}")


circle_obj = circle("Red", True, 2)
square_obj = square("Blue", False, 4)
triangle_obj = triangle("White", True, 5, 7)
circle_obj.disc()
circle_obj.Circumference()
square_obj.disc()
square_obj.area()
triangle_obj.disc()
triangle_obj.area()
