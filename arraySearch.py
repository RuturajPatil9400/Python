import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Search for elements greater than 30
indices = np.where(arr > 30)
print(indices)