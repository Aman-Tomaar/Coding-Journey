"""
*args    : allows you to pass multiple non-keyword arguments to a function. It collects them into a tuple.
**kwargs : allows you to pass multiple keyword arguments to a function. It collects them into a dictionary.
          * is a unpacking operator
"""

print("*args")


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 3, 6, 9))


def name(*args):
    for arg in args:
        print(arg, end=" ")


name("Sir", "Monsieur", "Strange", "Heart", "of", "Nowhere")


print("\n\n**kwargs")


def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


address(
    street="123 Fake St.",
    town="Nowhere",
    country="Paradox",
    continant="Terra Incognita",
    planet="Error 404",
    galaxy="The Inkwell Nebula",
    universe="The Omniverse of Fiction",
)

print("\n\nBoth *args and **kwargs")


def a_whole_person(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")


a_whole_person(
    "Sir",
    "Monsieur",
    "Strange",
    "Heart",
    "of",
    "Nowhere",
    street="123 Fake St.",
    town="Nowhere",
    country="Paradox",
    continant="Terra Incognita",
    planet="Error 404",
    galaxy="The Inkwell Nebula",
    universe="The Omniverse of Fiction",
)
