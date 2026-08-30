pi = 3.14159


def square(x):
    return x * x


def cube(x):
    return x * x * x


def circle_area(radius):
    return pi * square(radius)


def circle_circumference(radius):
    return 2 * pi * radius


def rectangle_area(length, width):
    return length * width


def rectangle_perimeter(length, width):
    return 2 * (length + width)
