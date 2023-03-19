list1=[]
x=input("enter name in list 1:")
while x!="q":
    list1.append(x)
    x=input("enter name in list 1:")
print(list1)
list2=[]
y=input("enter name in list 2:")
while y!="q":
    list2.append(y)
    y=input("enter name in list 2:")
print(list2)
def overlap(l1,l2):
    s1=set(l1)
    s2=set(l2)
    s= s1 & s2
    return list(s)
print("mutral frinds",overlap(list1,list2))