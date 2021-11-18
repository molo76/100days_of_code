from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.update_score()

    def update_score(self):
        self.write(f'Score:  {self.score}', False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', False, align=ALIGNMENT, font=FONT)

