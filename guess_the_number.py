"""
In this game, the computer will guess a random number and the player will try to guess what 
number it is. The game ends when the player manages to guess the number. Display the appropriate
score also. 
"""
import random
print("WELCOME TO THE GUESSING GAME")
c=1
while(c==1):
    a=int(input("Enter the lower limit: "))
    b=int(input("Enter the upper limit: "))
    if(b<a):
        print("Kindly enter a Valid Range")
    else:
        n=random.randint(a,b)
        print("GUESS THE NUMBER")
        m=int(input())
        c=0
        while(1):
            c=c+1
            if(n==m):
                print("Yippee!You guessed correctly.")
                print("Total Number Of Guesses=",c)
                break
            else:
                if(m<n):
                    print("Try Again!")
                    print("You Guessed Too Small")
                    m=int(input())
                else:
                    print("Try Again!")
                    print("You Guessed Too Large")
                    m=int(input())
    print("Do you want to play again?\nIf yes, then press '1' else press '0")
    c=int(input())
print("The Game Ends here....")
