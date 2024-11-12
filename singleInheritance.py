#Single Inheritance

class A :
    def m1(self):
        print("This m1 method is of class A")

    def m2(self,name,age):
        print(f"My name is {name} and my age is {age}.")

class B(A) :
    def m3(self):
        print("This m3 method is of class B")

    def m4(self,dept,college):
        print(f"My department is {dept} and my college name is {college}.")

obj1=B()

obj1.m1()
obj1.m2("Ruturaj Sambhaji Patil",21)
obj1.m3()
obj1.m4("CSE","Dr.D.Y.Patil College of Engineering,Kolhapur.")
