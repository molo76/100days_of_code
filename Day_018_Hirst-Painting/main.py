import turtle
import colorgram
from turtle import Turtle, Screen
from random import choice


def get_colors(image, no_of_colors):
    colors = colorgram.extract(image, no_of_colors)
    color_list = []
    for color in colors:
        color_to_add = (color.rgb.r, color.rgb.g, color.rgb.b)
        color_list.append(color_to_add)
    return color_list


def line_of_dots():
    for _ in range(10):
        t.dot(20, choice(rgb_colors))
        t.fd(40)


t = Turtle()
s = Screen()
t.speed(0)
s.colormode(255)
rgb_colors = get_colors("hirst_dots.jpg", 30)
t.pu()
t.goto(-160, -160)
t.hideturtle()


for _ in range(10):
    line_of_dots()
    t.goto(-160, t.ycor() + 40)

s.exitonclick()
