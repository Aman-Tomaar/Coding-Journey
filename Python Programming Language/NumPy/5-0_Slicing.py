import numpy as np

array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# array [start:end:step]
print(f"\n{array}\n\n")


print("FOR ROW")
print(f"Array at index 0 : \n{array[0]}")
print(f"Array at index 0 to 2 : \n{array[0 : 3]}")
print(
    f"Array at index 0 to end with step 2 : \n{array[::2]}"
)  # NOTE: No need to write if its going to end from start but need to use ':'
print(f"Array at index 0 to end but inverse: \n{array[::-1]}")
print(f"Array at index 0 to end but inverse while stepping 2: \n{array[::-2]}\n\n")


print("FOR COLUMN")
print(
    f"All elements at index 0: \n{array[:,0]}"
)  # need to use the : before , otherwise we will get error
# we can do the same indexing in this too
print(f"Elements of all Arrays from index 0 to 2: \n{array[:,0:2]}")
print(f"Elements of all Arrays from index 0 to end but with step 2: \n{array[:,::2]}")
print(
    f"Elements of all Arrays from index 0 to end but with step 1 and inverted: \n{array[:,::-1]}\n\n"
)

print("FOR BOTH ROW AND COLUMN SELECTION:")
print(f"Elements of 1st 2 rowns and 1st 2 columns: \n{array[:2,:2]}")
