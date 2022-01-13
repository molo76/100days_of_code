from random import randint

# New dictionary from list:
# new_dict = {new_key:new_value for item in list}

# New dictionary from existing dictionary:
# new_dict = {new_key:new_value for (key,value) in dict.items()}

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_scores = {name: randint(1, 100) for name in names}
passed_students = {student: score for (student, score) in student_scores.items() if score > 60}

print(student_scores)


