import random
import cv2

from matplotlib import pyplot as plt

bag1=bag2=bag3=10
total=bag1+bag2+bag3
num=val=60
flag=0
username=input("enter username:")

while total!=0:
    num = 60
    val = 60

#--------------------------------------------player picks bag
    while (num>3 or num<1):
        try:
            print(bag1,'-',bag2,'-',bag3)
            num=int(input("pick a bag(1,2,3):"))
            if num==1:
                if bag1==0:
                    print("bag1 fadia")
                    continue
            elif num==2:
                if bag2==0:
                    print("bag2 fadia")
                    continue
            else:
                if bag3==0:
                    print("bag3 fadia")
                    continue
        except ValueError:
            print("dont enter a charcter ")
            continue #try tni meil awel 
#--------------------------------------------player picks ball          
    while not (val<=5 and val>=1):
        try:
            val=int(input("pick how many balls(1,2,3,4,5):"))
            if num==1:
                if bag1-val>=0: 
                    bag1-=val
                else:
                    print("no enough balls")
                    continue
            elif num==2:
                if bag2-val>=0: 
                    bag2-=val
                else:
                    print("no enough balls")    
                    continue                
            elif num==3:
                if bag3-val>=0: 
                    bag3-=val
                else:
                    print("no enough balls")
                    continue                    
            else:
                print("no such bag")
        except ValueError:
            print("dont enter a charcter ")
            continue
        
        print("you took",val,"from bag number",num)
    total=bag1+bag2+bag3
    if total==0:
        flag+=1
        break
#-------------------------------------------- computer picks bag
    num = 60
    val = 60
    while (num>3 or num<1):
        #inclusive
        num= random.randint(1,3)
        if num==1:
            if bag1==0:
                break
        elif num==2:
            if bag2==0:
                break
        else:
            if bag3==0:
                break        
#-------------------------------------------- computer picks ball
    while not (val<=5 and val>=1):
        val= random.randint(1,5)
        if num==1:
            if bag1-val>=0: 
                bag1-=val
                print("computer took",val,"from bag number",num)
                break
            else:
                continue
        elif num==2:
                if bag2-val>=0: 
                    bag2-=val
                    print("computer took",val,"from bag number",num)
                    break
                else:
                    continue
        elif num==3:
            if bag3-val>=0: 
                bag3-=val
                print("computer took",val,"from bag number",num)
                break
            else:
                continue
        
#--------------------------------------------el winner
img=cv2.imread('w.jpg')
b,g,r=split(img)
img=cv2.merge(r,g,b)

if flag==1:
    print("player",username, "won")
    cv2.putText(img,"{username}won",(10,300),0,2,(0,0,255),5)
    plt.imshow(img)
    plt.show()
else:
    print("comp won")
    cv2.putText(img,"got you",(10,300),0,2,(0,0,255),5)
    plt.imshow(img)
    plt.show()