my_list = [10, 20, 30, 40, 50]

my_list.append(60)
my_list.insert(2, 25)
my_list.remove(40)
my_list[1] = 15

print("Modified List:", my_list)


print("Length of List:", len(my_list))
print("Index of 30:", my_list.index(30))
my_list.sort()
print("Sorted List:", my_list)
my_list.reverse()
print("Reversed List:", my_list)

squared_list = [x**2 for x in my_list]
print("Squared List:", squared_list)

new_list = my_list.copy()
print("Copied List:", new_list)

my_list.clear()
print("Cleared List:", my_list)
