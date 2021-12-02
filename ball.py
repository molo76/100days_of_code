from turtle import Turtle

class Ball(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.goto(starting_position)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        print(new_y)
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        print(self.y_move)

