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
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.Score}  High Score = {self.high_score}", align=ALIGNMENT, font=("Arial", SIZE, "normal"))


    def increase_score(self):
        self.Score += 1
        self.update_scoreboard()

    def reset(self):
        if self.Score > self.high_score:
            self.high_score = self.Score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.Score = 0
        self.update_scoreboard()


