from turtle import Turtle

MOVE_DISTANCE = 50

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color('White')
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x=x_cor, y=y_cor)

    def move_up(self):
        y_up = self.ycor() + 50
        self.goto(self.xcor(), y_up)

    def move_down(self):
        y_down = self.ycor() - 50
        self.goto(self.xcor(), y_down)
