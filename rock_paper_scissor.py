"""
try to solve with pseudocode:
 a) Player vs. computer.
 b) An interface with options.
 c) Checking the player against the computer.
 d) Returning the winner status.
 e) Ask if the player wants to play again.
"""
import random
print("WELCOME\nYou are invited to play rock paper scissor game.")
print("RULES:\n1.Scissor beats Paper\n2.Rock beats Scissor\n3.Paper beats Rock")
l=['rock','paper','scissor']
while(1):
    a=random.choice(l)
    n=input("What do you want to choose?")
    n=n.lower()
    if n in l:
        if(a==n):
            print(f"System too chose {a}\nDRAW!")
        elif(a=='rock'):
            if(n=='scissor'):
                print("System chose Rock\nSince,Rock beats Scissor,YOU LOST!")
            else:
                print("System chose Rock\nSince,Paper beats Rock,YOU WON!")
        elif(a=='paper'):
            if(n=='scissor'):
                print("System chose Paper\nSince,Scissor beats Paper,YOU WON!")
            else:
                print("System chose Paper\nSince,Paper beats Rock,YOU LOST!")
        else:
            if(n=='rock'):
                print("System chose Scissor\nSince,Rock beats Scissor,YOU WON!")
            else:
                print("System chose Scissor\nSince,Scissor beats Paper,YOU LOST!")
    else:
        print("Enter a valid option")
    print("Do you want to play again?\nif you want to play again,Press '1'\nelse Press '0'")
    b=int(input())
    if(b==0):
        print("The Game Ends....\nGoodBye!")
        break
