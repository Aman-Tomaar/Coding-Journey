import numpy as np

scores = np.array([85, 90, 55, 100, 88])

# Comparison operations
print(
    "Scores greater than 90:", scores > 90
)  # True for the element with value above 90
print(
    "Scores less than 60:", scores <= 60
)  # True for the element with value below and equal to 60
print("Scores equal to 88:", scores == 88)  # True for the element with value 88
print(
    "Scores not equal to 100:", scores != 100
)  # True for the element with value not equal to 100
scores[scores < 60] = 0
print(
    "Change the scores less than 60 to 0:", scores
)  # Change the scores less than 60 to 0
