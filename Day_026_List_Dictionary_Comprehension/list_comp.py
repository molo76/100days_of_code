# For Loop
numbers = [1, 2, 3]
new_list = []
for num in numbers:
    add_1 = num + 1
    new_list.append(add_1)

# new_list = [new_item for item in existing_list]
new_list = [num + 1 for num in numbers]
print(new_list)

doubled_numbers = [n * 2 for n in range(1, 5)]
print(doubled_numbers)

# conditional list comprehension
# new_list = [new_item for item in list if test]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
upper_names = [name.upper() for name in names if len(name) > 5]
