def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    z = x / y
    return z


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Adding {a}, {b} = {add(a, b)}")
print(f"Subtracting {a}, {b} = {subtract(a, b)}")
print(f"Multiplying {a}, {b} = {multiply(a, b)}")
print(f"Dividing {a}, {b} = {divide(a, b):.2f}")
