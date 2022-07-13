from turtle import Turtle
from snake import Snake
from food import Food




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self) :
        self.goto(0,0)
        self.write("Game Over.", align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.score +=1
        self.clear()
        self.update()
