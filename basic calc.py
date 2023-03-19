x=int(input("enter value 1;"))
y=int(input("enter value 2;"))
z=0
op=input("enter op")
if op=="*":
    z=x*y
elif op=="/":
    if y!=0:
        z=x/y
    else:
        z="infinity"
elif op=="+":
    z=x+y
elif op=="-":
    z=x-y
print("result=",z )
