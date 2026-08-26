item = []
price = []
quantity = []
total = 0
final = 0
while True:
    i = input("Enter the name of the Item you want to buy: ")
    p = float(input(f"Enter the price of {i} you want to buy: $"))
    q = int(input(f"Enter the quantity of {i} you want to buy: "))

    item.append(i.upper())
    price.append(p)
    quantity.append(q)

    x = input("Want to add more stuff to cart (Yes OR No): ")
    if x.lower() == "no" or x.lower() == "n":
        break

print("YOUR CART =>")
print(f"{'ITEM':^10} X {'QUANTITY':^10} X {'PRICE':^10} = {'Total':^10}")
for j in range(len(item)):
    total = quantity[j] * price[j]
    print(f"{item[j]:^10} X {quantity[j]:^10} X {price[j]:^10.2f} = {total:^10.2f}")
    final += total
print(f"{'Total Final => {final:.2f}':^30}")
