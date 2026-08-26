# Tuple => () Tuple is a collection which is ordered and unchangeable, Duplicates allowed, Faster than lists and sets.

print("Tuple")
fruits = (
    "apple",
    "banana",
    "cherry",
    "orange",
    "kiwi",
    "mango",
    "mango",
)  # Tuple
print(fruits)
print("\n")

print("Finding the length of the tuple")
print(len(fruits))  # Length of the tuple
print("\n")

print("Finding if 'banana' is in the tuple")
print("banana" in fruits)  # Check if item is in the tuple
print("\n")

print("Finding the index of 'orange' in the tuple")
print(fruits.index("orange"))  # Find the index of an item in the tuple
print("\n")

print("Counting the number of times 'mango' appears in the tuple")
print(fruits.count("mango"))  # Count the number of times an item appears in the tuple
print("\n")
