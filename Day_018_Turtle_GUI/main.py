from turtle import Turtle, Screen
from random import randint

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


for num in range(3, 21):
    pen_color = (randint(0,255), randint(0,255), randint(0,255))
    timmy.pencolor(pen_color)
    draw_shape(num)
















screen.exitonclick()
