from art import logo
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5


def difficulty_level(player_choice):
    if player_choice == "easy": 
        print("You selected 'easy', you have 10 guesses!\n")
        return EASY_LEVEL
    else: 
        print("You selected 'hard', you have 5 guesses!\n")
        return HARD_LEVEL


def check_number(player_guess, guesses_left):
    guesses_left -= 1
    if player_guess == number:
        print(f"You guessed correctly, the number was {number}. You win! Well done!\n")
        guesses_left = 0
        return guesses_left
    elif player_guess > number:
        print("Too high, you have to choose again!")
        print(f"You have {guesses_left} guesses left.\n") 
        return guesses_left
    else:
        print("Too low, choose again!")
        print(f"You have {guesses_left} guesses left.\n")
        return guesses_left


play = 'y'
while play == 'y':

    print(logo)
    print("Welcome to Number Wang! The Number Guessing Game!")
    print("I'm thining of a number between 1 and 100.")
    number = randint(1,100)
    guesses = difficulty_level(input("Choose a difficulty. Type 'easy' or hard: "))
    
    while guesses > 0:
        guess = int(input("Guess a number: "))
        guesses=(check_number(guess, guesses))
        if guesses == 0 and guess != number:
            print("You have run out of guesses, bad luck")
            play = input("Would you like to play again? Type 'y' or 'n': ")
        elif guess == number: 
            play = input("Would you like to play again? Type 'y' or 'n': ")
              
      
