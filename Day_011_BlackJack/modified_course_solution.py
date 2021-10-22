from random import choice
from os import system, name
from art import logo

def clear_screen():
  """Screen clear function determines OS type to product correct system command"""
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def deal_card():
    cards = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
    card = choice(cards)
    return card

def calculate_score(hand):
    hand_as_numbers = []
    picture_cards = ["Jack","Queen","King"]
    for card in hand:
        if card in picture_cards:
            hand_as_numbers.append(10)
        elif card == "Ace":
            hand_as_numbers.append(11)
        else:
            hand_as_numbers.append(card)                    
    score = sum(hand_as_numbers)
    if len(hand) == 2 and score == 21:
        score = 0
    if 11 in hand_as_numbers and score > 21:
        score -= 10
    return score

def compare_scores(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose, the computer had a Blackjack!"
    elif player_score == 0:
        return "You win! You had a Blackjack!"
    elif player_score > 21:
        return "You lose, you went bust!"
    elif computer_score > 21: 
        return "You win, the computer went bust!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print(logo)
    player_cards = []
    computer_cards = []
    
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    is_game_over = False
    
    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computers first card: {computer_cards[0]}")
        
        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else: 
            player_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_should_deal == 'y':
                player_cards.append(deal_card())
            else: 
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"    Your final hand: {player_cards}, final score: {player_score}")
    print(f"    Computers final hand: {computer_cards}, final score: {computer_score}")    
    print(compare_scores(player_score, computer_score))

while input("Do you want to play a game of blackjack? Type 'y' for yes, or 'n' for no: ") == 'y':
    clear_screen()
    play_game()