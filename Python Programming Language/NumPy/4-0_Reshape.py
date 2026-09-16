import numpy as np

# Create a 1D array with 12 elements
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original Array:\n", array)

# 1. 2 rows, 6 columns (2 * 6 = 12)
array_2_6 = array.reshape(2, 6)
print("\nReshaped to (2, 6):\n", array_2_6)

# 2. 3 rows, 4 columns (3 * 4 = 12)
array_3_4 = array.reshape(3, 4)
print("\nReshaped to (3, 4):\n", array_3_4)

# NOTE: array.reshape(4, 4) ya array.reshape(2, 4) mat likhna,
# kyunki 12 elements ko 16 ya 8 mein convert nahi kiya ja sakta (ValueError aayega).

# 3. 4 rows, 3 columns (4 * 3 = 12)
array_4_3 = array.reshape(4, 3)
print("\nReshaped to (4, 3):\n", array_4_3)

# 4. 3D Array (2 blocks, 2 rows, 3 columns = 12 elements)
array_3d_1 = array.reshape(2, 2, 3)
print("\nReshaped to 3D (2, 2, 3):\n", array_3d_1)

# 5. Another 3D layout (3 blocks, 2 rows, 2 columns = 12 elements)
array_3d_2 = array.reshape(3, 2, 2)
print("\nReshaped to 3D (3, 2, 2):\n", array_3d_2)

# 6. Using -1 (NumPy khud calculate kar leta hai baki dimension ko)
# 1 row, and automatically calculate columns (-1)
row_vector = array.reshape(1, -1)
print("\nReshaped to (1, -1) [Row Vector]:\n", row_vector)

# Automatically calculate rows (-1), and 1 column
col_vector = array.reshape(-1, 1)
print("\nReshaped to (-1, 1) [Column Vector]:\n", col_vector)
