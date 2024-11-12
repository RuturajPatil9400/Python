my_tuple = (10, 20, 30, 40, 50)

print("Length of Tuple:", len(my_tuple))

print("Index of 30:", my_tuple.index(30))

sorted_tuple = tuple(sorted(my_tuple))
print("Sorted Tuple:", sorted_tuple)

reversed_tuple = my_tuple[::-1]
print("Reversed Tuple:", reversed_tuple)

squared_tuple = tuple(x**2 for x in my_tuple)
print("Squared Tuple:", squared_tuple)

new_tuple = my_tuple
print("Copied Tuple:", new_tuple)

my_tuple = ()
print("Cleared Tuple:", my_tuple)
