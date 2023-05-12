#handcricket
from random import choice
li=[1,1,2,2,2,3,3,3,3]
litoss=["H","T"]
def tosss():
    global tos
    global toss
    tos=input("Toss: H or T? ")
    tos=tos.upper()
    print("Flipping coin... press enter",end="")
    none=input()
    toss=choice(litoss)
tosss()
bb=["bat","bowl"]
while tos not in ["H","T"]:
    print("invalid")
    print()
    tosss()
else:
    print("It's a",toss)
    if tos==toss:
        bplayer=input("bat or bowl? ")
        bplayer=bplayer.lower()
        print()
        ind=bb.index(bplayer)
        bcomp=bb[int(not ind)]
    else:
        bcomp=choice(bb)
        print("Computer has chosen to",bcomp)
        ind=bb.index(bcomp)
        bplayer=bb[int(not ind)]
if bplayer=="bat":
    print("You are batting")
    print()
    i,j=0,1
    runs=0
    while i!=j:
        i=input("Bat: ")
        j=choice(li)
        if len(i)==1:
            if "1"<=i<="3":
                i=int(i)
            else:
                print("invalid")
                i=0
            print("Ball: ",j)
            if i!=j:
                runs+=int(i)
            print("Your runs: ",runs)
            print()
        else:
            print("invalid")
    else:
        target=runs+1
        print("Bowled! The compter's target is",target)
        print("--------------")
        print()
        print("Start bowling, the computer is going to bat.")
    i,j=0,1
    while target>=0 and i!=j:
        i=input("Bowl: ")
        j=choice(li)
        if len(i)==1:
            if "1"<=i<="3":
                i=int(i)
            else:
                print("invalid")
                i=-1
            print("Computer's bat: ",j)
            if i!=j:
                target-=j
            print("Computer's target: ",target)
            print()
        else:
            print("invalid")
    else:
        if i==j:
            print("Compter bowled out!")
            if target>0:
                print("Congratulations! You win.")
            elif target==1:
                print("It's a draw.")
        else:
            if target>0:
                print("Congratulations! You win.")
            elif target==1:
                print("It's a draw.")
            else:
                print("Computer wins!")
elif bplayer=="bowl":
    print("You are bowling.")
    print()
    i,j=0,1
    runs=0
    while i!=j:
        i=input("Bowl: ")
        j=choice(li)
        if len(i)==1:
            if "1"<=i<="3":
                i=int(i)
            else:
                print("invalid")
                i=-1
            print("Computer's bat: ",j)
            if i!=j:
                runs+=j
            print("Computer's runs: ",runs)
            print()
        else:
            print("invalid")
    else:
        target=runs+1
        print("Computer bowled out!")
        print("Your target is",target)
        print()
        print("Start batting, the computer is going to bowl.")
    i,j=0,1
    while target>=0 and i!=j:
        i=input("Bat: ")
        j=choice(li)
        if len(i)==1:
            if "1"<=i<="3":
                i=int(i)
            else:
                print("invalid")
                i=0
            print("Ball: ",j)
            if i!=j:
                target-=int(i)
            print("Your target:",target)
            print()
        else:
            print("invalid")
    else:
        if i==j:
            print("Bowled out!")
            if target>0:
                print("Computer wins")
            elif target==1:
                print("It's a draw.")
        else:
            if target<0:
                print("Congratulations! You win.")
            elif target==1:
                print("It's a draw.")
            else:
                print("Computer wins!")
else:
    print("invalid")
