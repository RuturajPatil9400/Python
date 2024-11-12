import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

print("Slice from index 1 to 4:", arr[1:4])
print("Slice from start to index 3:", arr[:3])
print("Slice from index 3 to the end:", arr[3:])
print("Slice with step size of 2:", arr[::2])
print("Complete array:", arr[:])