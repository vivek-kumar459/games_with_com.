print(" 1 = ROCK\n 2 = PAPER\n 3 = SCISSOR")
c=int(input("Enter your choise (1, 2, 3) : "))

if (c == 1):
    print("You choose ROCK :")
elif(c == 2):
    print("You choose PAPER :")
elif(c == 3):
    print("You choose SCISSOR ")
else:
    print("INVALID CHOISE !!")

import random
a = random.randrange(1,4)
if (a == 1):
    print("COMPUTER choose ROCK :")
elif(a == 2):
    print("COMPUTER choose PAPER :")
else:
    print("COMPUTER choose SCISSOR")

if(c == 1 and a == 2):
    print("YOU LOSE !!")
elif(c==1 and a==3):
    print("YOU WON !!")
elif(c==2 and a==1):
    print("YOU WON !!")
elif(c==2 and a==3):
    print("YOU LOSE !!")
elif(c==3 and a==1):
    print("YOU LOSE !!")
elif(c==3 and a==2):
    print("YOU WON !!")
else:
    print("MATCH DRAW...!!")