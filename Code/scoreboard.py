from turtle import Turtle
ALIGNMENT = "center"
SIZE = 20
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.Score = 0
        self.write(f"Score = {self.Score}", align=ALIGNMENT, font=("Arial", SIZE, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.Score += 1
        self.clear()
        self.write(f"Score = {self.Score}", align=ALIGNMENT, font=("Arial", SIZE, "normal"))

    def lost(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=("Arial", SIZE, "bold"))


