import art
from random import randint
from game_data import data

def select_datasets(already_used):
    first = randint(0,49)
    second = randint(0,49)
    while first in already_used:
        first = randint(0,49)
    while second in already_used or second == first:
        second = randint(0,49)
    return [first,second]


def comparison(compare_a, compare_b):
    if compare_a['follower_count'] > compare_b['follower_count']:
        return compare_a['name'], compare_a['follower_count']
    if compare_a['follower_count'] < compare_b['follower_count']:
        return compare_b['name'], compare_b['follower_count']



used_datasets = []
datasets = select_datasets(used_datasets)
first_dataset = data[datasets[0]]
second_dataset = data[datasets[1]]
used_datasets.append(datasets)
current_score = 0

#debug here: 
print(first_dataset)
print(second_dataset)

print(f"Compare A: {first_dataset['name']}, {first_dataset['description']}, {first_dataset['country']}")
print(f"Against B: {second_dataset['name']}, {second_dataset['description']}, {second_dataset['country']}")

winner = comparison(first_dataset, second_dataset)[0]
print(winner)

choice = input("Who has more instragram followers, select 'a' or 'b': ")
if choice == 'a':
    choice = first_dataset['name']
elif choice == 'b':
    choice = second_dataset['name']
else: 
    print("You didnt type 'a' or 'b', you are the loser here")

if choice == winner:
    current_score += 1
    print(f"You're right, current score = {current_score}")
else: 
    print(f"Sorry you're wrong. Final score = {current_score}")

# print(first_dataset)
# print(second_dataset)
# print(used_datasets)

play = 'yes'

#print(art.logo)

#print(art.vs)


    # {
    #     'name': 'Instagram',
    #     'follower_count': 346,
    #     'description': 'Social media platform',
    #     'country': 'United States'
    # },