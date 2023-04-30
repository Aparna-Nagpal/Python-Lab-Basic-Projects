"""
A row of dashes represents the word to guess. If the player guesses a letter in the word, the 
script writes it in all its correct positions. The player has 10 turns to guess the word. You can easily 
customize the game by changing the variables.
"""
import random
print("WELCOME TO THE HANGMAN GAME!!")
l=['pencil','monkey','secret','colour','monster','hockey','happy']
a=random.choice(l)
guess_left=[
    
    """-------
        |    
        |
        |
        |
        |
        |
        |
    ------------""",
    """ -------
        |    |
        |    
        |
        |
        |
        |
        |
    ------------
    """, """
        -------
        |    |
        |    |
        |    
        |    
        |
        |
        |
    ------------
    """, """
        -------
        |    |
        |    |
        |    O
        |    
        |   
        |
        |
    ------------
    """, """
        -------
        |    |
        |    |
        |    O
        |    |
        |    
        |
        |
    ------------
    """, """
        -------
        |    |
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """, """
        -------
        |    |
        |    |
        |    O
        |    |
        |    |
        |    |
        |
    ------------""","""
        -------
        |    |
        |    |
        |    O
        |    |
        |   /|
        |    |
    ------------""","""
        -------
        |    |
        |    |
        |    O
        |    |
        |   /|\\ 
        |    |
        |
    ------------""","""
        -------
        |    |
        |    |
        |    O
        |    |
        |   /|\\
        |    |
        |   / 
    ------------""","""
        -------
        |    |
        |    |
        |    O
        |    |
        |   /|\\
        |    |
        |   / \\
    ------------"""
    ]
while(1):
    g=0
    n=10
    m=''
    while(n>0):
        f=0
        for i in a:
            if i in m:
                print(i,end=' ')
            else:
                f=1
                print("_",end=' ')
        if(f==0):
            print("YOU WON!!")
            g=1
            break
        v=input("\nGuess the letter: ")
        m=m+v
        if v not in a:
            n=n-1
            print(f"Wrong Guess\nYou now have {n} turns left to guess the right word")
        print(guess_left[10-n])
        if(n==0):
            print("YOU LOST")
            g=1
    if(g==1):
        print('Do you want to play play again?\nPress 1 to play again\nPress 0 to exit')
        h=int(input())
    if(h==0):
        print("GAME ENDS.....")
        break
