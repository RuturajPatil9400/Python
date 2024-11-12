my_dict = {
    "name": "Ruturaj",
    "Age": 21,
    "College": "D.Y.P.",
    "Department": "CSE",
    "Year_of_learning": "Third year"
}

my_dict["Country"] = "India"
my_dict["Age"] = 22

print("Modified Dictionary:", my_dict)

print("Length of Dictionary:", len(my_dict))

print("Is 'College' key in the dictionary?", "College" in my_dict)

sorted_dict = sorted(my_dict.keys())
print("Sorted Dictionary by keys:", sorted_dict)


sorted_dict_values = sorted(my_dict.values(), key=lambda x: str(x))
print("Sorted Dictionary by values:", sorted_dict_values)

new_dict = my_dict.copy()
print("Copied Dictionary:", new_dict)

my_dict.clear()
print("Cleared Dictionary:", my_dict)
