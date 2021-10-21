from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = randint(0,2)

game_images = [rock, paper, scissors]

if not player_choice >= 3 and not player_choice < 0 or player_choice not in [0,1,2,3,4,5,6,7,8,9]:
  print(game_images[player_choice])
  print("\nComputer chose:\n")
  print(game_images[computer_choice])

if (player_choice == computer_choice):
  print("It's a draw")
elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
  print('You lose')
elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
  print("You win")
else: 
  print("Whatever you typed was invalid, you lose.")
