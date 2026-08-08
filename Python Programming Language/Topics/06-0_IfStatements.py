name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"{name} you are {age} eligible to get a Driving License!!")
elif age < 0:
    print(f"{name} you haven't been born yet!!")
else:
    print(f"{name} you are only {age} years old! You are not eligible to get a Driving License yet!")
