import numpy as np

print("NumPy Functions")
print("1. np.zeros() - Create an array of zeros")
array1 = np.zeros((2, 3, 4))  # Create a 2x3x4 array of zeros
print(array1)

print("\n2. np.ones() - Create an array of ones")
array2 = np.ones((3, 2))  # Create a 3x2 array of ones
print(array2)

print("\n3. np.full() - Create an array filled with a specific value")
array3 = np.full((8, 3), 7)  # Create a 8x3 array filled with the value 7
print(array3)

print("\n4. np.eye() - Create an identity matrix")
array4 = np.eye(4)  # Create a 4x4 identity matrix
print(array4)

print("\n5. np.empty() - Create an uninitialized array")
array5 = np.empty((3, 3))  # Create a 3x3 uninitialized array
print(array5)  # use garbage value from memory

print("\n6. np.arange() - Create an array with a range of values")
array6 = np.arange(  # start, stop, step
    0, 100, 2
)  # Create an array with values from 0 to 100 with a step of 2
print(array6)

print("\n7. np.linspace() - Create an array with evenly spaced values")
array7 = np.linspace(  # start, stop, num {num is the number of samples to generate}
    0, 1, 5
)  # Create an array with 5 evenly spaced values between 0 and 1
print(array7)
