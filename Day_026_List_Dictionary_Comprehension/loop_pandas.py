import pandas

student_dict = {
    'student': ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie'],
    'score': [56, 87, 69, 92, 76, 71]
}


# Create dataframe from dict:
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through dataframe:
# for key,value in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame:
for (index, row) in student_data_frame.iterrows():
    #print(row)
    print(row.student)
    print(row.score)



