import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
colours = data['Primary Fur Color']

gray_count = colours.value_counts()['Gray']
cinnamon_count = colours.value_counts()['Cinnamon']
black_count = colours.value_counts()['Black']

colour_data = {
    'Fur Color': ['Grey', 'Cinnamon', 'Black'],
    'Count': [gray_count, cinnamon_count, black_count]
}
print(colour_data)

squirrel_color_data = pd.DataFrame(colour_data)
squirrel_color_data.to_csv('squirrel_colors.csv')