# Work with csv through importing csv module - tldr, use pandas instead
# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas
import pandas as pd
# get csv data from file into pandas
data = pd.read_csv('weather_data.csv')
print(data)
print('-----------\n')

# get column
print('# get column')
print(data.temp)
print('-----------\n')

# get column into a list
print('# get column into a list')
temperature_list = data.temp.to_list()
print(temperature_list)
print('-----------\n')

# get average of column, first manually
print('# get average of column, first manually')
total_temp = 0
for i in range(len(temperature_list)):
    total_temp += temperature_list[i]
print(round(total_temp / (len(temperature_list)), 2))

# then using inbuilt method .mean
print('# then using inbuilt function .mean')
print(round(data.temp.mean(), 2))
print('-----------\n')

# another useful method .max
print('# another useful method .max')
print(data.temp.max())
print('-----------\n')

# get row
print('# get row')
print(data[data.temp == data.temp.max()])
print('-----------\n')

# get row, then get column item from row
print('# get row, then get column item from row')
monday = data[data.day == 'Monday']
print(monday.temp)
monday_temp = monday.temp.to_string()
print(monday_temp)
print(type(monday_temp))
print('-----------\n')

# challenge, get column item, do something with it
print('# challenge, get column item, do something with it\n# in this case convert to F')
temp_in_f = (monday.temp * (9 / 5)) + 32
print(temp_in_f)

# create a dataframe from scratch
print('# create a dataframe from scratch')
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv('new_data.csv')