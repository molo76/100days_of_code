from os import system
from time import sleep
from data import MENU
from art import logo


def report():
    for resource in resources:
        if resource == 'water':
            print(f"Water: {resources['water']}ml")
        elif resource == 'milk':
            print(f"Milk: {resources['milk']}ml")
        elif resource == 'coffee':
            print(f"Coffee: {resources['coffee']}g")
        else:
            money = "{:.2f}".format(resources['money'])
            print(f"Money: £{money}")


def resource_check(chosen_drink):
    for ingredient in chosen_drink['ingredients']:
        amount_required = chosen_drink['ingredients'][ingredient]
        amount_available = resources[ingredient]
        if amount_required > amount_available:
            print(f"Sorry, there is not enough {ingredient} in the machine at present, please select an alternative.")
            return False
    return True


def insert_coins(amount_due, drink_name):
    total_inserted = 0
    printable_amount = "{:.2f}".format(amount_due)
    print(f"Your choice: {drink_name}. The cost is ${printable_amount}.")
    while total_inserted < amount_due:
        print("Please enter coins...")
        for coin in coins_accepted:
            inserted = int(input(f"how many {coin}?")) * coins_accepted[coin]
            total_inserted += inserted
        printable_total_inserted = "{:.2f}".format(total_inserted)
        if total_inserted < amount_due:
            print(f"${printable_total_inserted} is not enough please insert more coins")
        else:
            print(f"You have inserted ${printable_total_inserted}, thank you. ")
            if total_inserted > amount_due:
                change = "{:.2f}".format(round(total_inserted - amount_due, 2))
                print(f"Here is ${change} change.")


def make_drink(chosen_drink, drink_name):
    for ingredient in chosen_drink['ingredients']:
        resources[ingredient] -= chosen_drink['ingredients'][ingredient]
    resources['money'] += chosen_drink['cost']
    print("Making your drink now.....")
    wait = 0
    dots = ""
    while wait < 5:
        dots += "."
        print(dots)
        sleep(1)
        wait += 1
    print(f"\nHere is your {drink_name}...Enjoy!")


drinks = ['espresso', 'latte', 'cappuccino']

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0,
}

coins_accepted = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickels': 0.05,
    'cents': 0.01
}

power = True
system('clear')

while power:
    print(logo)
    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'report':
        report()
    elif user_choice == 'off':
        power = False
    else:
        if user_choice not in drinks:
            print("Drink choice not recognised, please try again.")
        else:
            beverage = MENU[user_choice]
            if resource_check(beverage):
                insert_coins(beverage["cost"], user_choice)
                make_drink(beverage, user_choice)
    sleep(2)
    system('clear')

