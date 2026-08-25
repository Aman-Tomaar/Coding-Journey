i = int(input("Enter the number you want to count down to: "))
for i in range(1,i+1):
    print(i)

j = int(input("Enter the number you want to skip: "))
for i in range(1,i+1):
    if i == j:
        continue
    else:
        print(i)

k = int(input("Enter the number on which you want to break the loop: "))
for i in range(1,i+1):
    if i == k:
        break
    else: 
        print(i)