item = input("Enter the Item you wanna buy: ")
price = float(input(f"Enter the price of 1 x {item}: "))
quantity = int(input(f"Enter the quantity of {item}: "))

Total = price * quantity
print(f"Your total of {quantity} x {item} which is {price} each would be : ${Total}")