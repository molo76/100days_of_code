fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
# Original:

# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + " pie")


make_pie(4)

