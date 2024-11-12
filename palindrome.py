list1=["M","A","A","M"]
copyList1=list1.copy()
copyList1.reverse()

if(list1==copyList1):
    print("Palindrome")
else:
    print("Not palindrome")

list2=[]

list2.append(input("Enter element : "))
list2.append(input("Enter element : "))
list2.append(input("Enter element : "))

copyList2=list2.copy()
copyList2.reverse()

if(list2==copyList2):
    print("Palindrome")
else:
    print("Not palindrome")
