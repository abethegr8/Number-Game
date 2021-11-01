#import random library
import random

#the number is a random integer
#the random uses a function call randit per the python library 
#random.randit(a,b), returns a random  integer N such that a <= N <= b. 
#https://docs.python.org/3/library/random.html
guessThisNumber = random.randint(1,20)

#for loop, including ranch which means you get 3 tries at guessing the number 
for i in range(0,3): 
    print(f"Welcome to Abraham's Number game, you have 3 chances to guess the number from 1 - 20! Good Luck!")
    #simple input statment assigning user to the input from the user 
    user = int(input("Please enter the number you have guessed: "))
    #if statement if the user actually guessed the number 
    if user == guessThisNumber: 
        print("Congratulations!!")
        print(f" you are correct the number is: {guessThisNumber}")
        break
if user != guessThisNumber: 
    print(f"Your guess is incorrect the number is {guessThisNumber}")


