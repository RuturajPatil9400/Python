#Data types in python

intNum=12
floatNum=12.12
complexNum=4+8j
String="Ruturaj Sambhaji Patil."
List=["Ruturaj",12,12.12,4+8j,4,3,6,1,657]
Tuple=("Ruturaj",12,12.12,4+8j,4,3,6,1,657)
Set={"Ruturaj",12,12.12,4+8j,4,3,6,1,657}
Dictionary={
    "intNum" : 12,
    "floatNum" : 12.12,
    "complexNum" : 4+8j,
    "String" : "Ruturaj Sambhaji Patil."
    
}
Boolean=True
Frozenset=frozenset({1,4,3,5})
Range=range(5)

noneType=None


variables=[intNum,floatNum,complexNum,String,List,Set,Tuple,Dictionary,Boolean,Frozenset,Range,noneType]

for var in variables :
    print(f"Value : {var} , Type : {type}")