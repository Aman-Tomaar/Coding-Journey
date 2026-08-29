capitals = {
    "India": "New Delhi",
    "USA": "Washington D.C.",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "Canada": "Ottawa",
}

print(f"The capital of India is: {capitals['India']}")
print(
    f"If i try to get a key which is not in the dictionary, it will return: {capitals.get("France", "Not Found")}\n\n"
)

print("Adding a new key-value pair to the dictionary")
capitals["France"] = "Paris"
print(f"Updated dictionary: {capitals}\n\n")

print("Changing the value of an existing key in the dictionary")
capitals["France"] = "Lyon"
print(f"Updated dictionary: {capitals}\n\n")

print("Removing a key-value pair from the dictionary")
del capitals["France"]
print(f"Updated dictionary: {capitals}\n\n")

print("Poping a key-value pair from the dictionary")
print(f"Popped value: {capitals.pop("Germany")}")
print(f"Updated dictionary: {capitals}\n\n")

print("Popping the last key-value pair from the dictionary")
print(f"Popped value: {capitals.popitem()}")
print(f"Updated dictionary: {capitals}\n\n")


print("Getting all the keys from the dictionary")
print(f"Keys: {capitals.keys()}\n\n")

print("Getting all the values from the dictionary")
print(f"Values: {capitals.values()}\n\n")

print("Getting all the key-value pairs from the dictionary")
print(f"Items: {capitals.items()}\n\n")

print("Copying the dictionary")
capitals_copy = capitals.copy()
print(f"Copy of the dictionary: {capitals_copy}\n\n")

print("Clearing the dictionary")
capitals.clear()
print(f"Updated dictionary: {capitals}\n\n")
