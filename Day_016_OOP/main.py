from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system
from time import sleep
from art import logo

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

power = True

while power:
    print(logo)
    user_choice = input(f"\nWhat would you like? ({menu.get_items()}): ").lower()
    print(user_choice)
    if user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_choice == 'off':
        power = False
    else:
        beverage = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(beverage):
            money_required = "{:.2f}".format(round(beverage.cost,2))
            print(f"The cost of your drink is ${money_required}")
            if money_machine.make_payment(beverage.cost):
                coffee_maker.make_coffee(beverage)
            else:
                print("You need to pay the correct amount, or more. Change is given")
        sleep(3)
        system('clear')
