#Concept of Method Overriding

class A :
    def m1(self):
        print("This m1 method is of class A")

    def m2(self):
        print(f"My name is Ruturaj Patil and my age is 21.")

class B(A) :

    def m1(self):
        super().m1()
        print("This m1 method is of class B")

    def m2(self):
        super().m2()
        print(f"My friend's name is Suraj Patil and his age is 23 ")

    

obj1=B()

obj1.m1()
obj1.m2()
