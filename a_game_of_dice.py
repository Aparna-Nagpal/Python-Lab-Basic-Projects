"""
In this project, we will look at how you can emulate a player throwing a set of dice. Then we 
will look at how you can store these dice in a pile the player wants to keep. you write a game where 
you throw dice to determine the outcome, this is one way to store the results for later use. example, 
normal dice with six eyes. The program will work no matter how many eyes your dice have.
"""
import random
print("Welcome\nLet's play a game of Dice")
while(1):
    p1=input("Enter the name of player1=")
    p2=input("Enter the name of player1=")
    a=random.randint(1,6)
    b=random.randint(1,6)
    print(f"{p1} score:{a}\n{p2} score:{b}")
    if(a>b):
        print(f"{p1} Won")
    elif(b>a):
        print(f"{p2} Won")
    else:
        print("Draw")
    print("Do you want to play again?\nPress 1 else Press 0")
    if(int(input())==0):
        print("Game over....\nGoodBye!")
        break
