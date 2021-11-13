from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed = 0


def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.bk(10)

def clockwise():
    tim.rt(10)

def counter_clockwise():
    tim.lt(10)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=tim.reset)


screen.exitonclick()
