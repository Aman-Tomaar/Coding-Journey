class Animals:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is not sleeping")


class Dog(Animals):

    def speak(self):
        print(f"{self.name} is speaking: WOOF!!")


class Cat(Animals):

    def speak(self):
        print(f"{self.name} is speaking: MEOW!!")


class Mouse(Animals):

    def speak(self):
        print(f"{self.name} is speaking: SQUEEK!!")


dog = Dog("Ghevar")
cat = Cat("Meowth")
mouse = Mouse("Micky")

print(f"{dog.name} is alive: {dog.is_alive}")
dog.eat()
dog.sleep()
dog.speak()
print("\n" + "-" * 30 + "\n")

print(f"{cat.name} is alive: {cat.is_alive}")
cat.eat()
cat.sleep()
cat.speak()
print("\n" + "-" * 30 + "\n")

print(f"{mouse.name} is alive: {mouse.is_alive}")
mouse.eat()
mouse.sleep()
mouse.speak()
