#Method Overloading Concept
class A :
    def m1(self,*args) :
        sum=0
        for i in args :
            sum=i+sum
        
        print(f"Total sum is {sum}")

obj1=A()

obj1.m1(1,2)
obj1.m1(1,2,3,4,5,6)
obj1.m1(1,2,3,4,5,6,7,8,9,10)
obj1.m1(4,6,2,7)
obj1.m1(2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2)
obj1.m1(1)
