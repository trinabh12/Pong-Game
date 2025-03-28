from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        if self.l_score == 20 or self.r_score == 20:

            if self.l_score == 20:
                self.goto(0, 0)
                self.write("Left-side won", align="center", font=("italic", 85, "normal"))

            else:
                self.goto(0, 0)
                self.write("Right-side won", align="center", font=("italic", 85, "normal"))



