#Program 1
def show(n) :
    if(n==0):
        return 
    else :
        print(n,end=" ")
        show(n-1)

show(5)
print()

#Program 2
def fact(n) :
    if(n==0 or n==1):
        return 1
    else :
        return n*fact(n-1)
n=fact(5)
print(n)
