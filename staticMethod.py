#Static methods

class A :
    def m1():                                                              #Static method                                                        
        print("This m1 method is of class A")

    def m2(self,name,age):
        print(f"My name is {name} and my age is {age}.")

class B(A) :
    def m3():                                                                        #Static method
        print("This m3 method is of class B")

    def m4(self,college):
        print(f"I am a student of {college}.")

class C(B) :
    def m5():                                                                          #Static method
        print("This m5 method is of class C")

    def m6(self,dept,year_of_learning):
        print(f"Currently, I am pursuing a Bachelor’s degree in {dept} in {year_of_learning} ")


class D(C) :
    def m7():                                                                              #Static method
        print("This m5 method is of class C")
    
    def m8(self,student_ID):
        print(f"And my student ERN number is {student_ID}")


obj1=D()

A.m1()
obj1.m2("Ruturaj Sambhaji Patil",21)
B.m3()
obj1.m4("Dr.D.Y.Patil College of Engineering,Kolhapur")
C.m5()
obj1.m6("CSE","third year.")
D.m7()
obj1.m8("ERN123")
