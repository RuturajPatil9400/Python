list=[]

i=1

while i<=10 :
    square=i*i
    list.append(square)
    print(i,"*",i,"=",square)
    i += 1

print(list)


i=0

while i<len(list):                                          #traverse (because we are traversing on existing data which is in list )
    print("Element present at index",i,"is",list[i])
    i += 1 