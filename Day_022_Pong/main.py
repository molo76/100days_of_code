from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

game_is_on = True
while game_is_on:
    screen.update()
    screen.listen()
    screen.onkey(r_paddle.go_up, 'Up')
    screen.onkey(r_paddle.go_down, 'Down')
    screen.onkey(l_paddle.go_up, 'a')
    screen.onkey(l_paddle.go_down, 'z')





screen.exitonclick()