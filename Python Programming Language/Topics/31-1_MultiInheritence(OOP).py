# Multiple Inheritance : Inherit from more than one parent class
#                       c(a, b) : c is child class of a and b

# Multilevel Inheritance : Inherit from a class which is already inherited from another class
#                         c(b) <- b(a) <- a[parent class]


print("1. Multiple Inheritance")


class prey:
    def flee(self, prey_name):
        print(f"{prey_name} is fleeing")


class predator:
    def hunt(self, predator_name):
        print(f"{predator_name} predator is hunting")


class rabbit(prey):
    pass


class hawk(predator):
    pass


class fox(prey, predator):  # Multiple Inhertence
    pass


rabbit_obj = rabbit()
hawk_obj = hawk()
fox_obj = fox()

rabbit_obj.flee("Ratata the rabbit")
hawk_obj.hunt("Hawkins the hawk")
fox_obj.flee("Vulpix the fox")
fox_obj.hunt("Nine Tails the fox")

print("\n2. Multilevel Inheritance")


class animal:  # Multilevel Inhertence as animal is a parent class of extinct and extinct is a parent class of dodo
    def __init__(
        self, name
    ):  # I didnt had to use self.name = name in the extinct & dodo class because it is already inherited from the animal class
        self.name = name


class extinct(animal):
    def alive(self):
        print(f"{self.name} is extinct")


class dodo(extinct):
    pass


dodo_obj = dodo("Dodo bird")
dodo_obj.alive()
