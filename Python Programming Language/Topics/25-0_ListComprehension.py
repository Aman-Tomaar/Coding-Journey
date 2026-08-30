# list comprehension = [expression for value in iterable if condition]
doubles = [x * 2 for x in range(1, 11)]
triples = [x * 3 for x in range(1, 11)]
squares = [x * x for x in range(1, 11)]
print(doubles)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(triples)
print(squares)
print("\n\n")

fruits = ["apple", "banana", "orange"]
fruits_upper = [fruit.upper() for fruit in fruits]
# fruits_upper = [fruit.upper() for fruit in ["apple", "banana", "orange"]] we can replace the fruits with the whole list
print(fruits_upper)
fruits_char = [fruit[0] for fruit in fruits]
print(fruits_char)
