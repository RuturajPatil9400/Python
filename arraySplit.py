import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Split the array into 3 equal parts
split_arr = np.array_split(arr, 3)
print(split_arr)