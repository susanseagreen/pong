from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player2_score, align="center", font=("Courier", 80, "normal"))

    def player1_point(self):
        self.player1_score += 1
        self.update_scoreboard()

    def player2_point(self):
        self.player2_score += 1
        self.update_scoreboard()
