from turtle import Turtle, Screen
import random

screen = Screen()

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()

turtles = [t1, t2, t3, t4, t5, t6]
colours = ["red", "green", "blue", "orange", "brown", "purple"]


def initialise_turtles():
    y_cord = -150
    for turtle in turtles:
        y_cord += 50
        turtle.pu()
        turtle.shape('turtle')
        chosen_colour = random.choice(colours)
        colours.remove(chosen_colour)
        turtle.color(chosen_colour)
        turtle.setpos(-300, y_cord)

initialise_turtles()

def race():
    for racer in turtles:
        racer.speed(random.randint(0, 10))
    while True:
        for racer in turtles:
            racer.fd(10)

for turtle in turtles:
    screen.listen()
    screen.onkey(key="space", fun=race)



screen.exitonclick()