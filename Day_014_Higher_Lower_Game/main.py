import os
import art
import random
from random import randint
from game_data import data

def select_datasets(already_used, previous_winner):
    if current_score == 0:
        first = random.choice(data)
        second = random.choice(data)
    else:
        first = previous_winner
        second = random.choice(data)
    while first["name"] in already_used:
        first = random.choice(data)
    while second["name"] in already_used or second["name"] == first["name"]:
        second = random.choice(data)
    return [first,second]

def comparison(compare_a, compare_b):
    if compare_a['follower_count'] > compare_b['follower_count']:
        return compare_a['name'], compare_a['follower_count']
    if compare_a['follower_count'] < compare_b['follower_count']:
        return compare_b['name'], compare_b['follower_count']

play = True
current_score = 0
used_datasets = []
first_dataset = {}
second_dataset = {}

while play == True:
    datasets = select_datasets(used_datasets, second_dataset)
    first_dataset = datasets[0]
    second_dataset = datasets[1]

    os.system('clear')
    print(art.logo)
    if current_score > 0:
        print(f"You're right, current score = {current_score}")
    print(f"\nCompare A: {first_dataset['name']}, {first_dataset['description']}, {first_dataset['country']}")
    print(art.vs)
    print(f"\nAgainst B: {second_dataset['name']}, {second_dataset['description']}, {second_dataset['country']}")
    
    winner = comparison(first_dataset, second_dataset)[0]
    # print(winner)
    
    choice = input("Who has more instragram followers, type 'A' or 'B': ").upper()
    if choice == 'A':
        choice = first_dataset['name']
    elif choice == 'B':
        choice = second_dataset['name']
    else: 
        print("You didnt type 'A' or 'B', you are the loser here")
    
    if choice == winner:
        current_score += 1
    else:
        os.system('clear') 
        print(art.logo)
        print(f"Sorry you're wrong. Final score = {current_score}")
        play = False