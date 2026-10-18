import numpy as np

array = np.array(
    [
        [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
        [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
        [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]],
    ]
)  # if we dont use " " then it will give error bcause each elemnt of array should be of same length, so we use " " to make it same length.

print(
    array.ndim
)  # returns number of dimensions (1 = 1D Array, 2 = 2D Array, 3 = 3D Array)
print(
    array.shape
)  # returns a tuple of integers that represent the shape ( Depth[Layers], Rows, Columns )

word = (
    array[2, 0, 0]
    + array[2, 0, 1]
    + array[1, 2, 2]
    + array[0, 0, 0]
    + array[1, 1, 1]
    + array[0, 2, 0]
    + array[0, 1, 1]
    + array[2, 2, 2]
    + array[0, 2, 1]
    + array[0, 1, 1]
    + array[0, 0, 0]
    + array[1, 2, 2]
    + array[2, 0, 1]
)  # [][][] is known as chain indexing, first index is for depth, second index is for row and third index is for column.
# But in numpy we got multidimentionalindexing [<depth>, <row>, <column>] its faster then using [<depth>][<row>][<column>].

print(word)
