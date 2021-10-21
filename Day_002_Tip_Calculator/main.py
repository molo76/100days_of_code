print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? £"))
tip_percent = int(input("What % tip would you like to give? 10, 12 or 15? "))
people_paying = int(input("How many people to split the bill? "))

per_person_payment = round((tip_percent / 100 * total_bill + total_bill) / people_paying, 2)
final_amount = "{:.2f}".format(per_person_payment)
print(f"Each person should pay: £{final_amount}")

