import random
x=input("choose the game you want to start or enter exit to exit:\n 1-toss a coin\n 2-get a random number\n 3-random choice\n")
if x=="exit":
    print("goodbye")
elif x=="1" :
    value=random.randint(0,1)
    if value=="1":
        print( "a coin was tosed and landed on: tail")
    else:
        print( "a coin was tosed and landed on: heads")
elif x=="2" :
    y=input("choose a range of values ex(0,10):")
    listy=y.split(",")
    value2=random.randint(int(listy[0]),int(listy[1]))
    print("a random number is",value2)
elif x=="3":
    z=input("enter a list of choices(x,y,z..):")
    listz=z.split(",")
    if "Papa Johns" in listz: #weight le papa johns
        
    value3=random.choice(listz)
    print(value3)
else :
    print("entered a wrong input")