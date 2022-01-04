#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt', 'r') as invited_names:
    names_list = invited_names.readlines()
    for i in range(len(names_list)):
        names_list[i] = names_list[i].strip('\n')

with open('./Input/Letters/starting_letter.txt', 'r') as letter_template:
    template = letter_template.read()

for name in names_list:
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', 'w') as letter_to_send:
        letter_to_send.write(template.replace('[name]', name))


