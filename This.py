class Student:
    def _init_(self, name, age):
        self.name = name  
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


student1 = Student("Ruturaj", 21)

student1.display()