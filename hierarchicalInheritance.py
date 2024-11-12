#Hierarchical Inheritance

class A :
    def m1(self):
        print("This m1 method is of class A")

    def m2(self,name,age):
        print(f"My name is {name} and my age is {age}.")

class B(A) :
    def m3(self):
        print("This m3 method is of class B")

    def m4(self,college):
        print(f"I am a student of {college}.")

class C(A) :
    def m5(self):
        print("This m5 method is of class C")

    def m6(self,dept,year_of_learning):
        print(f"Currently, I am pursuing a Bachelor’s degree in {dept} in {year_of_learning} ")


class D(A) :
    def m7(self):
        print("This m5 method is of class C")
    
    def m8(self,student_ID):
        print(f"And my student ERN number is {student_ID}")


obj1=B()
obj1.m1()
obj1.m2("Ruturaj Sambhaji Patil",21)
obj1.m3()
obj1.m4("Dr.D.Y.Patil College of Engineering,Kolhapur")


obj2=C()
obj2.m1()
obj2.m2("Ruturaj Sambhaji Patil",21)
obj2.m5()
obj2.m6("CSE","third year.")


obj3=D()
obj3.m1()
obj3.m2("Ruturaj Sambhaji Patil",21)
obj3.m7()
obj3.m8("ERN123")








