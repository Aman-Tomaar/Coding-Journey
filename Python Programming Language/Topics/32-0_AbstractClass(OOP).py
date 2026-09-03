# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.
#                 They can contain abstract methods, which are declared but have no implementation.
#                 Abstract classes benefits:
#                   1. Prevents instantiation of the class itself
#                   2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car is starting.")

    def stop(self):
        print("Car is stopping.")


class Bike(Vehicle):
    def start(self):
        print("Bike is starting.")

    def stop(self):
        print("Bike is stopping.")


# Creating objects of the subclasses
car = Car()
bike = Bike()

# Calling the methods
car.start()  # Output: Car is starting.
car.stop()  # Output: Car is stopping.
bike.start()  # Output: Bike is starting.
bike.stop()  # Output: Bike is stopping.
