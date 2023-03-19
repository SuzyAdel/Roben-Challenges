list=[]
x=input("enter val:")
while x!="q":
    if x.isdigit():
        list.append(int(x))
    x=input("enter val:")
print(list)
print("maximum=",max(list),"minumum=",min(list)) 
    
    