from turtle import Turtle, Screen
from random import randint
from random import choice

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.shape("classic")
num = 1

# for _ in range(15):
#     if _ % 2 == 0:
#         timmy.pd()
#     else:
#         timmy.pu()
#     timmy.fd(10)

def draw_shape(sides):
    for side in range(sides):
        timmy.fd(20)
        timmy.rt(360 / sides)


# for num in range(3, 21):
#     pen_color = (randint(0,255), randint(0,255), randint(0,255))
#     timmy.pencolor(pen_color)
#     draw_shape(num)

# Randomn Walk

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

# for num in range(1000):
#     pen_color = (random_color())
#     timmy.pensize(10)
#     timmy.speed(0)
#     timmy.pencolor(pen_color)
#     options = [0, 90, 180, 270]
#     timmy.seth(choice(options))
#     timmy.fd(30)


timmy.speed(0)


def draw_spirograph(offset):
    for num in range(int(360 / offset)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + offset)


draw_spirograph(10)
screen.exitonclick()
