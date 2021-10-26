from art import logo
from random import randint

def check_number(player_guess, guesses_left):
    guesses_left -= 1
    if player_guess == number:
        print(f"You guessed correctly, you win! Well done!")
        guesses_left = 0
        return guesses_left
    elif player_guess > number:
        print(f"Too high, you have to choose again!") 
        return guesses_left
    else:
        print(f"Too low, choose again!")
        return guesses_left

play = 'y'
while play == 'y':

    print(logo)
    print("Welcome to Number Wang! The Number Guessing Game!")
    print("I'm thining of a number between 1 and 100.")
    number = randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or hard: ")

    if difficulty == "easy": 
        print("You selected 'easy', you have 10 guesses!")
        guesses = 10
    else: 
        print("You selected 'hard', you have 5 guesses!")
        guesses = 5
    
    while guesses > 0:
        print(guesses)
        guess = int(input("Guess a number: "))
        guesses=(check_number(guess, guesses))
        if guesses == 0 and guess != number:
            print("You have run out of guesses, bad luck")
            play = input("Would you like to play again? Type 'y' or 'n': ")
        elif guess == number: 
            play = input("Would you like to play again? Type 'y' or 'n': ")
              
      
