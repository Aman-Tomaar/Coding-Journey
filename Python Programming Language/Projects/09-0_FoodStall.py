menu = {
    "Pizza": 3.50,
    "Burger": 3.00,
    "Steam momos": 1.50,
    "Fried momos": 1.70,
    "Roll": 1.50,
    "Chaap": 5.00,
    "Fries": 1.25,
}
cart = []
ncart = []
total = 0

print("******** MENU *********")
for key, value in menu.items():
    print(f"{key:15} : ${value}")
print("***********************\n\n")

while True:
    food = input("Select an item from the list (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food.capitalize()) is not None:
        cart.append(food.capitalize())
    elif menu.get(food.capitalize()) is None:
        ncart.append(food.capitalize())


print("******** YOUR CART *********")
for food in cart:
    total += menu.get(food)
    print(f"{food.capitalize():15} : {menu.get(food)}")
print(f"{"Total":15} : {total}")
print("****************************")
print("Stuff not found on the stall: ")
for nfood in ncart:
    print(nfood)
