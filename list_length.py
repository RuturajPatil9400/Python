"""
#Program 1
def list_lenghth(set) :
    print(len(set))

list_lenghth([10,11,12,13,14])


#Program 2
def list_lenghth(set) :
    for val in set :
        print(val,end=" ")

list_lenghth([10,11,12,13,14])


#Program 3
def cal(n) :
    fact=1
    i=1
    while i<=n :
        fact=fact*i
        i += 1

    print(fact)
    return fact

cal(3)

"""

#Program 4
def conversion(USD) :
    Rs=USD*80
    print(Rs)
    return Rs

conversion(80)








