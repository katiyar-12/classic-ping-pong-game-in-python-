from turtle import Turtle

class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(-30,180)



    def scoreboard(self):
        self.clear()
        self.write(f"{self.l_score}   {self.r_score}",align="center",font=("Courier",60,"normal"))

    def l_point(self):
        self.l_score += 1

    def r_point(self) :
        self.r_score += 1







