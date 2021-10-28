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

used_datasets = []
datasets = select_datasets(used_datasets)
first_dataset = data[datasets[0]]
second_dataset = data[datasets[1]]
used_datasets.append(datasets)


print(first_dataset)
print(second_dataset)
print(used_datasets)

play = 'yes'

#print(art.logo)

#print(art.vs)


    # {
    #     'name': 'Instagram',
    #     'follower_count': 346,
    #     'description': 'Social media platform',
    #     'country': 'United States'
    # },