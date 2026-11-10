#here is the code for guessing the number game
import random
num = random.randint(1, 100)

print("WELCOME TO THIS GAME...!!")
print("IN THIS YOU HAVE TO GUSSE NUMBER BETWEEN 1 to 100")

gusse = int(input("Enter your gut feeling number : "))
atmpt = 1

while True:
   
    if (gusse < num):
        print("Think little bit HIGH..! ")
        atmpt += 1
    elif(gusse > num):
        print("Think little bit LOW..!")
        atmpt +=1
    else:
        print("Congrats You got it..!!")
        break

    gusse = int(input("Try with another number : "))

print("The number was : ", num)

print("You gussed this number with : ", atmpt , "Attempts")