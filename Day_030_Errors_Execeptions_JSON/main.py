#FileNotFoundError
# with open('somefile.txt') as file:
#     file.read()

#KeyError
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non_existent_key']

#IndexError
# fruit_list = ['apple', 'pear', 'banana']
# print(fruit_list[3])

#TypeError
# text = 'abc'
# print(text + 5)

# try: 'something that may cause an exception'
# except: 'do this if there was an exception'
# else: 'do this if there were no exceptions'
# finally: 'do this no matter what happens'


#Example:

try:
    file = open('data.txt')
    a_dictionary = {'key': 'dictionary value'}
    print(a_dictionary['key'])
except FileNotFoundError:
    file = open('data.txt', 'w')
    file.write('something')
except KeyError as error_message:
    print(f'The key {error_message} does not exist!')
else:
    content = file.read()
    print(content)
finally:
    file.close()