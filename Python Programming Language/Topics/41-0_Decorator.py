# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator


def add_sprinkles(func):
    def wrapper(*args, **kwargs):  # if not add *args, **kwargs here we will get error
        print("*You add Sprinkles 🎉*")
        func(*args, **kwargs)  # if not add *args, **kwargs here we will get error

    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):  # if not add *args, **kwargs here we will get error
        print("*You add Fudge 🍫*")
        func(*args, **kwargs)  # if not add *args, **kwargs here we will get error

    return wrapper


@add_sprinkles
@add_fudge
def get_icecream(flavor):
    print(f"Here is your {flavor} Ice Cream")


get_icecream("Choclate")
