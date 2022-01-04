from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WRAP_SNAKE = False

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Nokia 3310 Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall or wrap.
    if WRAP_SNAKE:
        if snake.head.xcor() >= 300:
            snake.head.setx(-300)
        elif snake.head.xcor() <= -300:
            snake.head.setx(300)
        elif snake.head.ycor() >= 300:
            snake.head.sety(-300)
        elif snake.head.ycor() <= -300:
            snake.head.sety(300)
    else:
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
