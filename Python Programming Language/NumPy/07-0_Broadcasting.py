import numpy as np

# Broadcasting is a powerful mechanism that allows NumPy to work with arrays
# of different shapes when performing arithmetic operations.
# Rules of Broadcasting:
# 1. If the arrays do not have the same number of dimensions,
#    the shape of the one with fewer dimensions is padded with ones on its leading (left) side.
# 2. If the shape of the two arrays does not match in any dimension,
#    the array with shape equal to 1 in that dimension is stretched to match the other shape.
# 3. If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)

print(f"Adding array1 and array2 results is \n{array1 + array2}\n\n")
# Broadcasting will occur here as array1 (1, 4) and array2 (4, 1) both has 1 in each dimention,
# so they can be broadcasted to a common shape of (4, 4) for the addition operation.

array3 = np.array([[1, 2, 3], [4, 5, 6]])
array4 = np.array([[1], [2]])

print(array3.shape)
print(array4.shape)

print(f"Adding array3 and array4 results is \n{array3 + array4}\n\n")
