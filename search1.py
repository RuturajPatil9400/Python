tup=(1,4,9,16,25,36,49,64,81,100)

num=int(input("Enter number : "))

i=0

while i<len(tup):
    if(tup[i]==num):
        print(tup[i],"is present in the tuple at",i,"index")
    i += 1

print("End of a code")