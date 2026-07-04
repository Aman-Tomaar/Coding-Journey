x = float(input("Enter 1st Digit: "))
y = float(input("Enter 2nd Digit: "))
z = int(input("\nChoose One 1 => Addision\n           " \
"2 => Subtraction\n           " \
"3 => Multiplication\n           " \
"4 => Division\nEnter Your Choice: "))

if z == 1:
    print(f"{x} + {y} = {x+y}")
elif z == 2:
    print(f"{x} - {y} = {x-y}")
elif z == 3:
    print(f"{x} * {y} = {x*y}")
elif z == 4:
    print(f"{x} / {y} = {x/y}")
else:
    print("Invalid Choice!!")