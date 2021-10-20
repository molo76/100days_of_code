import art
from random import randint
from os import system, name

def clear_screen():
  """Screen clear function determines OS type to product correct system command"""
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def card_value(card):
    value = 0
    if card in picture_cards:
        #print(f"It's a picture - {card}")
        value = 10
    elif card == "Ace":        
        #print(f"it's an Ace!!! - {card}")
        if player_score <= 10:
            value = 11
        else: 
            value = 1
    else:
        #print(f"It's just a number - {card}")
        value = card
    return value

def deal_player(player_score):
    if player_score == 0:
        player_cards.append(cards[randint(0,11)])
        player_cards.append(cards[randint(0,11)])    
        for card in player_cards:
            player_score += card_value(card)
    else:
        player_cards.append(cards[randint(0,11)])
        player_score += card_value(player_cards[-1])
    return player_score

def deal_computer(computer_score):
    if computer_score == 0:
        computer_cards.append(cards[randint(0,11)])
        computer_score += card_value(computer_cards[0])
    elif computer_score <= 16: 
        computer_cards.append(cards[randint(0,11)])
        computer_score += card_value(computer_cards[-1])
    return computer_score

cards = [2,3,4,5,6,7,8,9,"Jack","Queen","King","Ace"]
picture_cards = ["Jack","Queen","King"]

computer_score = 0
computer_cards = []

player_score = 0
player_cards = []

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play == 'y':
    clear_screen()
    print(art.logo)
    player_score = deal_player(player_score)
    print(f"\nYour cards: {player_cards}, current score: {player_score}")
    computer_score = deal_computer(computer_score)
    print(f"Computer's first card: {computer_cards}")
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while another_card == 'y':
        player_score = deal_player(player_score)
        if player_score > 21: 
            another_card = 'n'
        else:
            print(f"Your cards: {player_cards}, current score: {player_score}")
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if player_score > 21 or another_card == 'n':
        computer_deal = True
        while computer_score <= 21 and computer_deal:
            computer_score = deal_computer(computer_score)
            if computer_score >= 17 and computer_score <=21:
                computer_deal = False
        computer_deal = False
        print(f"\nYour final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    if player_score > 21:
        print("You went over, bust! You lose")
    if player_score <= 21 and computer_score < player_score:
        print("You win!")
    if player_score <= 21 and computer_score > 21: 
        print("Computer went bust, you win!") 
    if player_score <= 21 and computer_score > player_score and computer_score <= 21:
        print("Computer wins, you Lose!") 
    # play = input("Would you like to play again? Type 'y' or 'n': ")
    

    

