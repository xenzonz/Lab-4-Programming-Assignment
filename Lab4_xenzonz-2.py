"""
Docstring for Lab4_xenzonz_2
i. LAB 4: Guess the Number - Hangman Style
ii. Sam Cocquyt
iii. Player tries to guess a random number between 1 to 15. Each incorrect guess reveals another part of a hangman drawing.
    Will also give feedback if guess is too high or too low.
iv. No starter code
v. 2/8/2026
"""

import random

user_input = input("Guess a number (1-15): ").strip()
guess = int(user_input)
#test
print(guess)

def main():
    hangman_stages = [r'''
+-------+
|       |
|   
|   
|   
|   
==========''', r'''
+-------+
|       |
|       O
|   
|   
|   
==========''', r'''
+-------+
|       |
|       O
|       I
|   
|   
==========''', r'''
+-------+
|       |
|       O
|     .-I
|   
|   
==========''', r'''
+-------+
|       |
|       O
|     .-I-.
|   
|   
==========''', r'''
+-------+
|       |
|       O
|     .-I-.
|      /
|   
==========''', r'''
+-------+
|       |
|       O
|     .-I-.
|      / \
|   
==========''']

    secret_number = random.randint(1, 15)
    wrong_guesses = 0
    #test
    print(f"secret number is {secret_number}")

#run main function
main()




        
