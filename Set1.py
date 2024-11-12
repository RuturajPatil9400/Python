my_set = {10, 20, 30, 40, 50}

my_set.add(60)
my_set.remove(40) 
my_set.add(25)
my_set.discard(40)  
my_set.discard(20)  
my_set.add(15)

print("Modified Set:", my_set)

print("Length of Set:", len(my_set))

print("Does 30 exist in the set?", 30 in my_set)

sorted_set = sorted(my_set)
print("Sorted Set:", sorted_set)

reversed_set = sorted_set[::-1]
print("Reversed Set:", reversed_set)

squared_set = {x**2 for x in my_set}
print("Squared Set:", squared_set)

new_set = my_set.copy()
print("Copied Set:", new_set)

my_set.clear()
print("Cleared Set:", my_set)
