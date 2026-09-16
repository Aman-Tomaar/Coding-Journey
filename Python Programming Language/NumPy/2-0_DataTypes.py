import numpy as np

print("int")
int_array = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(int_array)
print(int_array.dtype)  # dtype is data type
print(f"{int_array.nbytes} bytes\n\n")  # nbytes is no of bytes

print("float")
float_array = np.array([1, 2, 3, 4, 5], dtype=np.float16)
print(float_array)
print(float_array.dtype)  # dtype is data type
print(f"{float_array.nbytes} bytes\n\n")  # nbytes is no of bytes

print("bool")
bool_array = np.array([1, 0, 1, 0, 1], dtype=np.bool_)  # 0 is False and 1 is True
print(bool_array)
print(bool_array.dtype)  # dtype is data type
print(f"{bool_array.nbytes} bytes\n\n")  # nbytes is no of bytes

print("string")
string_array1 = np.array([1, 2, 3, 4, 5], dtype=np.str_)
print(string_array1)
print(string_array1.dtype)  # dtype is data type
print(f"{string_array1.nbytes} bytes\n")  # nbytes is no of bytes
string_array2 = np.array(["hello", "world"], dtype=np.str_)
print(string_array2)
print(string_array2.dtype)  # dtype is data type
print(f"{string_array2.nbytes} bytes\n")  # nbytes is no of bytes
string_array3 = np.array(
    ["apple", "orange", "banana"], dtype=np.str_("<U4")
)  # <U4 means unicode string of length 4
print(string_array3)
print(string_array3.dtype)  # dtype is data type
print(f"{string_array3.nbytes} bytes\n")  # nbytes is no of bytes

print("complex")
complex_array = np.array([1, 2, 3, 4, 5], dtype=np.complex64)
print(complex_array)
print(complex_array.dtype)
print(f"{complex_array.nbytes} bytes\n\n")  # nbytes is no of bytes

print("object")  # we can store any type of data in object array,
# but it is not recommended to use it for numerical computations as it is slower than other data types.
# It is mainly used for storing mixed data types or custom objects.
object_array = np.array([1, "strange", 3.0, 4, True], dtype=np.object_)
print(object_array)
print(object_array.dtype)
print(f"{object_array.nbytes} bytes\n\n")  # nbytes is no of bytes

print("astype() method")
int_array1 = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(int_array1)
float_array5 = int_array1.astype(np.float64)
print(float_array5)
print(float_array5.dtype)  # dtype is data type
print(f"{float_array5.nbytes} bytes\n\n")  # nbytes is no of bytes


print("datetime")
datetime_array = np.array(
    ["2023-01-01", "2023-01-02", "2023-01-03"], dtype=np.datetime64
)
print(datetime_array)
print(datetime_array.dtype)
print(f"{datetime_array.nbytes} bytes\n\n")  # nbytes is no of bytes
