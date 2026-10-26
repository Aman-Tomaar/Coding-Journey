import numpy as np

array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("Aggregate Functions in NumPy\n")
print("1. np.sum() - Sum of array elements")
sum_result = np.sum(array)  # Sum of all elements in the array
print(sum_result)

print("\n2. np.mean() - Mean of array elements")
mean_result = np.mean(array)  # Mean of all elements in the array
print(mean_result)

print("\n3. np.std() - Standard deviation of array elements")
std_result = np.std(array)  # Standard deviation of all elements in the array
print(std_result)

print("\n4. np.var() - Variance of array elements")
var_result = np.var(array)  # Variance of all elements in the array
print(var_result)

print("\n5. np.min() - Minimum value in the array")
min_result = np.min(array)  # Minimum value in the array
print(min_result)

print("\n6. np.max() - Maximum value in the array")
max_result = np.max(array)  # Maximum value in the array
print(max_result)

print("\n7. np.argmin() - Index of the minimum value in the array")
argmin_result = np.argmin(array)  # Index of the minimum value in the array
print(argmin_result)

print("\n8. np.argmax() - Index of the maximum value in the array")
argmax_result = np.argmax(array)  # Index of the maximum value in the array
print(argmax_result)

print("\n9. np.cumsum() - Cumulative sum of array elements")
cumsum_result = np.cumsum(array)  # Cumulative sum of all elements in the array
print(cumsum_result)

print("\n-----------------------------")
print("Aggregate Functions with Axis\n")
print("1. np.sum() with axis=0 - Sum of array elements along the first axis (columns)")
sum_axis0_result = np.sum(array, axis=0)  # Sum along the first axis (columns)
print(sum_axis0_result)

print("\n2. np.sum() with axis=1 - Sum of array elements along the second axis (rows)")
sum_axis1_result = np.sum(array, axis=1)  # Sum along the second axis (rows)
print(sum_axis1_result)

# NOTE: axis=0 -> columns, axis=1 -> rows
# we can use this in other aggregate functions as well like mean, std,
# var, min, max, argmin, argmax, cumsum etc.
