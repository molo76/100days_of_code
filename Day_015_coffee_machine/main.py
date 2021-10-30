from data import MENU


def report():
    for resource in resources:
        if resource == 'water':
            print(f"Water: {resources['water']}ml")
        elif resource == 'milk':
            print(f"Milk: {resources['milk']}ml")
        elif resource == 'coffee':
            print(f"Coffee: {resources['coffee']}g")
        else:
            print(f"Money: £{resources['money']}")


def resource_check(chosen_drink):
    print(chosen_drink)
    for ingredient in chosen_drink['ingredients']:
        amount_required = chosen_drink['ingredients'][ingredient]
        amount_available = resources[ingredient]
        if amount_required > amount_available:
            print(f"Not enough {ingredient} in machine at present, {amount_required} required, {amount_available} available ")
            return False
    return True


def insert_coins(amount_due):
    total_inserted = 0
    printable_amount = "{:.2f}".format(amount_due)
    print(f"The cost of your chosen drink is ${printable_amount}")
    while total_inserted < amount_due:
        print("Please enter coins...")
        for coin in coins_accepted:
            inserted = int(input(f"how many {coin}?")) * coins_accepted[coin]
            total_inserted += inserted
        printable_total_inserted = "{:.2f}".format(total_inserted)
        if total_inserted < amount_due:
            print(f"${printable_total_inserted} is not enough please insert more coins")
        else:
            print(printable_total_inserted)
            if total_inserted > amount_due:
                change = round(total_inserted - amount_due, 2)
                print(f"You inserted ${printable_total_inserted}, here is ${change} change.")


def make_drink(chosen_drink):
    


resources = {
    'water': 300,
    'milk': 20,
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

while power:
    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'report':
        print(report())
    elif user_choice == 'off':
        power = False
    else:
        beverage = MENU[user_choice]
        if resource_check(beverage):
            insert_coins(beverage["cost"])
            make_drink(beverage)







# TODO: 1 - print report
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