# Set => {} Set is a collection which is unordered and unindexed, Duplicates not allowed.

print("Set")
fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}  # Set
print(fruits)
print("\n")

print("Finding the length of the set")
print(len(fruits))  # Length of the set
print("\n")

print("Finding if 'banana' is in the set")
print("banana" in fruits)  # Check if item is in the set
print("\n")

print("Adding a new fruit to the set")
fruits.add("pear")  # Add new item
print(fruits)
print("\n")

print("Removing 'banana' from the set")
fruits.remove("banana")  # Remove item
print(fruits)
print("\n")

print("Removing a random item from the set")
print(fruits.pop())  # Remove a random item from the set
print(fruits)
print("\n")

print("Clearing the set")
fruits.clear()  # Clear the set
print(fruits)
print("\n")
