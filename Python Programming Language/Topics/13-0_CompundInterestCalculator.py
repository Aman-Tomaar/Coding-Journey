principle = 0 
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle: "))
    if principle <= 0:
        print("Enter a value grater then 0")
print(f"Your principle is {principle}")
print("\n")

while rate <= 0:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("Enter a value grater then 0")    
print(f"Your rate is {rate}")
print("\n")

while time <= 0:
    time = int(input("Enter the time: "))
    if time <= 0:
        print("Enter a value grater then 0")
print(f"Your time is {time}")
print("\n")    

print("Your final amout is: ", principle*pow((1 + rate / 100), time))