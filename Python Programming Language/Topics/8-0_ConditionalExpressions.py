# Ternery Operator : X if <condition> else Y

print("**** EVEN OR ODD ****")
num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(f"Number is: {result}")

print("**** MAXIMUM NUM ****")
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
max_num = f"1st num i.e. :{a}" if a > b else f"2st num i.e. :{b}"
print(f"Max num is => {max_num}")

print("**** MINIMUM NUM ****")
c = int(input("Enter 1st number: "))
d = int(input("Enter 2nd number: "))
min_num = f"1st num i.e. :{c}" if c > d else f"2st num i.e. :{d}"
print(f"Min num is => {min_num}")