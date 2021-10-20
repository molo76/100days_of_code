from os import system, name
import art

print(art.logo)
print("Welcome to the secret auction program")
run = True

bids = {}

def clear_screen():
  """Screen clear function determines OS type to product correct system command"""
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def winner():
  highest_bid = 0
  winner = ""
  for name, bid_amount in bids.items():
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = name
  winning_bid = "{:.2f}".format(highest_bid)
  print(f"The winning bidder is {winner}, with a bid of £{winning_bid}") 


while run == True:
  name = input("What is your name?: ")
  bid = input("How much do you bid?: £")
  bids[name] = float(bid)
  keep_bidding = input("Are there any other bidders? Type 'yes' or 'no'.")
  if keep_bidding == "yes":
    run = True
    clear_screen()
  elif keep_bidding == "no":
    run = False
    clear_screen()
    winner()
  else: 
    keep_bidding = input("Input unrecognised. Are there any other bidders? Type 'yes' or 'no'.")
