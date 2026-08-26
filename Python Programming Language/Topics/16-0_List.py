# List => [] List is a collection which is ordered and changeable, Duplicates allowed.

print("List")
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  # List
print(fruits)

print("\n")
print("Changing cherry to grapes in the list")
fruits[2] = "grapes"  # Changeable
print(fruits)

print("\n")
print("Adding a new fruit to the list at the end")
fruits.append("pear")  # Add new item
print(fruits)

print("\n")
print("Removing banana from the list")
fruits.remove("banana")  # Remove item
print(fruits)

print("\n")
print("Inserting blueberry at index 2")
fruits.insert(2, "blueberry")  # Insert item at index 2
print(fruits)

print("\n")
print("Sorting the list")
fruits.sort()  # Sort the list
print(fruits)

print("\n")
print("Reversing the list")
fruits.reverse()  # Reverse the list
print(fruits)

print("\n")
print("Finding the index of orange in the list")
index = fruits.index("orange")
print(f"Index of orange: {index}")

print("\n")
print("Counting the number of times mango appears in the list")
count = fruits.count("mango")
print(f"Number of times mango appears: {count}")

print("\n")
print("Clearing the list")
fruits.clear()  # Clear the list
print(fruits)
