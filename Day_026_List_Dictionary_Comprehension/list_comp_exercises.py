numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:
squared_numbers = [num **2 for num in numbers]
#Write your code 👆 above:
print(squared_numbers)

#####################################

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [num for num in numbers if num % 2 == 0]

#Write your code 👆 above:

print(result)

#####################################

with open('file1.txt') as f1:
    f1_list = f1.read().splitlines()
with open('file2.txt') as f2:
    f2_list = f2.read().splitlines()

print(f1_list)
print(f2_list)
if len(f1_list) > len(f2_list):
    longer_list = f1_list
    shorter_list = f2_list
else:
    longer_list = f2_list
    shorter_list = f1_list

result = [int(num) for num in longer_list if num in shorter_list]
print(result)
