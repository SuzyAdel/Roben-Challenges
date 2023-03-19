#it is cold in here SUZY
temp=float(input("enter temp"))
x=input("the temp entered is c or f:")
if x=="c"or x=="C":
    temp2=(temp*1.8)+32
    print("the temp is=",temp2,"F")
elif x=="f"or x=="F":
    temp2=(temp-32)/1.8
    print("the temp is=",temp2,"C") 
else:
    print("letter error")


    

