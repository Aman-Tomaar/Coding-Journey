# list comprehension = [expression for value in iterable if condition]

nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
print(f"Prostive no. in Nums = {[num for num in nums if num >= 0]}")
print(f"Negative no. in Nums = {[num for num in nums if num < 0]}")
print(f"Even no. in Nums = {[num for num in nums if num % 2 == 0]}")
print(f"Odd no. in Nums = {[num for num in nums if num % 2 != 0]}")

grades = [30, 45, 69, 21, 97, 72, 10]
print([f"Passed :{grade}" for grade in grades if grade >= 30])
print([f"Failed :{grade}" for grade in grades if grade < 30])
