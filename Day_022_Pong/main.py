from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    screen.listen()
    screen.onkey(r_paddle.go_up, 'Up')
    screen.onkey(r_paddle.go_down, 'Down')
    screen.onkey(l_paddle.go_up, 'a')
    screen.onkey(l_paddle.go_down, 'z')
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Right player misses
    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.left_point()

    # Left player misses
    if ball.xcor() < -420:
        ball.reset_position()
        scoreboard.right_point()



screen.exitonclick()
