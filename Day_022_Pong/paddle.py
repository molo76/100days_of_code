from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)
        self.goto(starting_position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
