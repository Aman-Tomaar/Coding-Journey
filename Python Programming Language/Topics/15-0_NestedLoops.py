import time

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()
    time.sleep(1)
