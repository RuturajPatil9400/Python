# Sorting a list of tuples based on the second value
pairs = [(1, 2), (3, 1), (5, 4)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(3, 1), (1, 2), (5, 4)]