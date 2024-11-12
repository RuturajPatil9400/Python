# Sorting a list of dictionaries based on a key 'age'
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
sorted_people = sorted(people, key=lambda x: x['age'])
print(sorted_people)  # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]