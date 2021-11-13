from turtle import Turtle, Screen
import random

screen = Screen()

t1 = Turtle(shape="turtle")
t2 = Turtle(shape="turtle")
t3 = Turtle(shape="turtle")
t4 = Turtle(shape="turtle")
t5 = Turtle(shape="turtle")
t6 = Turtle(shape="turtle")
finish_line = Turtle()

turtles = [t1, t2, t3, t4, t5, t6]
colours = ["red", "green", "blue", "orange", "brown", "purple"]

def create_finish_line():
    finish_line.speed(3)
    finish_line.hideturtle()
    finish_line.pu()
    finish_line.setpos(250, 200)
    finish_line.setheading(270)
    finish_line.pd()
    finish_line.fd(350)


def initialise_turtles():
    y_cord = -150
    for turtle in turtles:
        y_cord += 50
        turtle.pu()
        chosen_colour = random.choice(colours)
        colours.remove(chosen_colour)
        turtle.color(chosen_colour)
        turtle.setpos(-300, y_cord)


def race():
    race_in_progress = True
    for racer in turtles:
        racer.speed(random.randint(0, 10))
    while race_in_progress:
        for racer in turtles:
            if racer.xcor() % 5 == 0:
                racer.speed(random.randint(0, 10))
            distance = random.randint(0, 25)
            racer.fd(distance)
            if racer.xcor() > 250:
                race_in_progress = False


create_finish_line()
initialise_turtles()
for turtle in turtles:
    screen.listen()
    screen.onkey(key="space", fun=race)
screen.exitonclick()