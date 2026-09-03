# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                  Object must have the minimum necessary attributes/methods
#                  "If it looks like a duck and quacks like a duck, it must be a duck."
#                  (It doesn't matter if all of them has the same parent class or not, as long as they have the same methods/attributes)


class Animal:

    alive = True


class Dog(Animal):

    def speak(self):
        return "Woof!"


class Cat(Animal):

    def speak(self):
        return "Meow!"


class Car:
    alive = (
        False  # Adding alive attribute to Car class to avoid error in the loop below
    )

    def speak(
        self,
    ):  # as this has the same speak function as the other classes, it can be used in the same way
        return "Vroom!"


classes = [Dog(), Cat(), Car()]

for cls in classes:
    print(cls.speak(), end=" ")  # Output: Woof! Meow! Vroom!
    print(
        f"Is it alive? :{cls.alive}"
    )  # for thhis we need to put alive attribute in car class as well, otherwise it will give an error.
