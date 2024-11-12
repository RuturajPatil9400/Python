my_frozenset = frozenset([10, 20, 30, 40, 50])

print("Frozenset:", my_frozenset)

another_frozenset = frozenset([40, 50, 60, 70])

union_frozenset = my_frozenset | another_frozenset
print("Union of Frozensets:", union_frozenset)

intersection_frozenset = my_frozenset & another_frozenset
print("Intersection of Frozensets:", intersection_frozenset)

print("Is 30 in the frozenset?", 30 in my_frozenset)

print("Length of Frozenset:", len(my_frozenset))
