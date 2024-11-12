#Slicing of a string

#Positive Slicing

str="I am a coder."                     #0123456789101112

print(str[0:13])
print(str[ :13])
print(str[0:len(str)])
print(str[0: ])

print(str[1:5])
print(str[4:8])
print(str[2:6])

#Negative Slicing

#str=-12-11-10-9-8-7-6-5-4-3-2-1

str = "I am a coder."

print(str[-13:])
print(str[:-14:-1])
print(str[-len(str):])
print(str[:-1])

print(str[-10:-6])
print(str[-9:-5])
print(str[-12:-8])



