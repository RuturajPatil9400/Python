#Multiple Inheritance

class A :
    def m1(self):
        print("This m1 method is of class A")

    def m2(self,name,age):
        print(f"My name is {name} and my age is {age}.")

class B() :
    def m3(self):
        print("This m3 method is of class B")

    def m4(self,college):
        print(f"I am a student of {college}.")

class C() :
    def m5(self):
        print("This m5 method is of class C")

    def m6(self,dept,year_of_learning):
        print(f"Currently, I am pursuing a Bachelor’s degree in {dept} in {year_of_learning} ")


class D(A,B,C) :
    def m7(self):
        print("This m5 method is of class C")
    
    def m8(self,student_ID):
        print(f"And my student ERN number is {student_ID}")


obj1=D()

obj1.m1()
obj1.m2("Ruturaj Sambhaji Patil",21)
obj1.m3()
obj1.m4("Dr.D.Y.Patil College of Engineering,Kolhapur")
obj1.m5()
obj1.m6("CSE","third year.")
obj1.m7()
obj1.m8("ERN123")
