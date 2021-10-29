from data import MENU


def report():
    if user_choice == 'report':
        for resource in resources:
            if resource == 'water':
                print(f"Water: {resources['water']}ml")
            elif resource == 'milk':
                print(f"Milk: {resources['milk']}ml")
            elif resource == 'coffee':
                print(f"Coffee: {resources['coffee']}g")
            else:
                print(f"Money: £{resources['money']}")

# def resource_check(beverage):
#     for resource in resources:

# def accept_coinage():


resources = {
  'water': 300,
  'milk': 200,
  'coffee': 100,
  'money': 0,
}

power = True

while power:
    # TODO: 1 - print report
    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'report':
        print(report())
    elif user_choice == 'off':
        power = False
    else:
        beverage = MENU[user_choice]
    print(beverage)





# TODO: 2 - check resources sufficient
# TODO: 3 - process coins
# TODO: 4 - check transaction successful
# TODO: 5 - make coffee!

# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0




# Please insert coins.
# how many quarters?: 0
# how many dimes?: 0
# how many nickles?: 0
# how many pennies?: 0
# Sorry that's not enough money. Money refunded.