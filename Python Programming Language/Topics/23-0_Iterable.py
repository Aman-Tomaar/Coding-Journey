# Iterable: Data Structures which can be iterated over. Examples include lists, tuples, dictionaries, sets, and strings.

print("Iterating over different data structures:\n")
print("List:")
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item, end=" ")
print("\n\n")

print("Tuple:")
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item, end=" ")
print("\n\n")

print("Dictionary:")
my_dict = {"a": 1, "b": 2, "c": 3}
print("Keys in Dictionary:")
for key in my_dict:
    print(key, end=" ")
print("\n\n")
print("Values in Dictionary:")
for value in my_dict.values():
    print(value, end=" ")
print("\n\n")
print("Key-Value pairs in Dictionary:")
for key, value in my_dict.items():
    print(key, value, end=" ")
print("\n\n")

print("Set:")
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item, end=" ")
print("\n\n")

print("String:")
my_string = "Hello World!"
for char in my_string:
    print(char, end=" ")
print("\n\n")
