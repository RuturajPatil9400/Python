n=int(input("Enter number : "))

i=1
count=0

while i<=n :
    if (n%i==0) :
        count += 1
        
    i += 1
        


if(count==2):
    print("Number is prime.")

else :
    print("Number is not prime.")
