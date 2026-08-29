import random

print("Generating random number between 1 and 10:")
print(random.randint(1, 10), "\n")  # Generates a random integer between 1 and 10

print("Generating random float between 0.0 and 1.0:")
print(random.random(), "\n")  # Generates a random float between 0.0 and 1.0

print("Generating random item from a list:")
print(
    random.choice(["apple", "banana", "cherry"]), "\n"
)  # Randomly selects an item from the list

print("Generating random sample of 5 unique numbers from 1 to 100:")
print(
    random.sample(range(1, 100), 5), "\n"
)  # Randomly selects 5 unique numbers from the range
print("Shuffling a list:")
a = [1, 2, 3, 4, 5]
random.shuffle(a)
print("[1, 2, 3, 4, 5]")  # Shuffles the list in place
print(a, "\n")  # Shuffles the list in place

print("Generating random number with Gaussian distribution (mean=0, stddev=1):")
print(
    random.gauss(0, 1), "\n"
)  # Generates a random number with Gaussian distribution (mean=0, stddev=1)
