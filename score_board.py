from turtle import Turtle
from food import Food


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 370)
        self.color("white")
        self.write(f"Score:{self.score}", align="center", font=('Lobster', 24, 'normal'))
        self.speed("fastest")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Lobster', 24, 'normal'))

    def score_counter(self):
        self.score += 1
        self.clear()  # Clear previous score
        self.write(f"Score:{self.score}", align="center", font=('Lobster', 24, 'normal'))
