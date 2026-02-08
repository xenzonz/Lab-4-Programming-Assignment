"""
Docstring for Lab4_xenzonz_2
i. LAB 4: Guess the Number - Hangman Style
ii. Sam Cocquyt
iii. Player tries to guess a random number between 1 to 15. Each incorrect guess reveals another part of a hangman drawing.
    Will also give feedback if guess is too high or too low.
iv. No starter code
v. 2/8/2026
"""
#print("TEST122")
import random

# user input function
def user_input_guess():
    #asks user to guess a number between 1 to 15

    while True: #while loop to keep asking if error
        try: #catch user error

            guess = int(input("Guess a number (1-15): ").strip())

            if 1 <= guess <=15:
                return guess
            else:
                print("Out of range! Enter a number from 1 to 15.")
                
        except ValueError: 
            print("Enter a whole number.")
    



        
    
#run user_input_guess
#user_input_guess()

#main logic function
def main(): 
    #hangman images in a list
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
    
    #main logic
    #CHANGE TO 1, 15 AFTER TESTING
    secret_number = random.randint(1, 15)
    wrong_guesses = 0
    max_wrong = len(hangman_stages) - 1

    print("Guess a number from 1 to 15. Dont get hanged!")
    print(f"You can be wrong {max_wrong} times before you get hanged.")
    print(hangman_stages[wrong_guesses])

    #test
    #print(f"secret number is {secret_number}")

    while True:
        guess = user_input_guess()

        #win if statement
        if guess == secret_number:
            print(f"Congrats! The secret number was {secret_number}. You live!!!")
            break
        
        #too low or too high number check
        if guess < secret_number:
            print(f"Too low! Try again.")
        else:
            print(f"Too high! Try again.")
        
        #add 1 if guessed wrong, print image, and then loop
        wrong_guesses += 1
        print(hangman_stages[wrong_guesses])
        #test
        #print(f"TESTwrong guesses: {wrong_guesses}")
        
        #lose if statement
        if wrong_guesses == max_wrong:
            print(f"You lost. The secret number was {secret_number}.")
            break

        
    

#run main function
main()




        
