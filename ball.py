from turtle import Turtle
import random
RANDOM_DIRECTION = [-1, 1]
SPEED = 10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.x_move = SPEED * RANDOM_DIRECTION[random.randint(0, 1)]
        self.y_move = SPEED * RANDOM_DIRECTION[random.randint(0, 1)]

    def keep_moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move = -1 * self.y_move

    def paddle_hit(self):
        self.x_move = -1 * self.x_move

    def refresh(self):
        self.goto(0, 0)