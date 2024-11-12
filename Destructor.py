class MyClass:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age
        print(f"Object created with name: {self.name} and age: {self.age}")

    def __del__(self):  # Destructor
        print(f"Object with name {self.name} and age {self.age} is being destroyed")

obj = MyClass("Ruturaj", 21)
del obj  # Destructor will be called here
