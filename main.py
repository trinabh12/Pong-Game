from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
p_left = Paddle(-380, 0)
p_right = Paddle(380, 0)
ball = Ball()
score = ScoreBoard()
screen.listen()
screen.onkey(p_left.move_up, "w")
screen.onkey(p_left.move_down, "s")

screen.onkey(p_right.move_up, "Up")
screen.onkey(p_right.move_down, "Down")
game_on = True
hit_speed = 1
while game_on:


    if 280 < ball.ycor() or ball.ycor() < -280:
        ball.bounce()

    time.sleep(0.05/hit_speed)
    ball.keep_moving()
    screen.update()

    if ball.distance(p_right) < 50 and ball.xcor() > 360 or ball.distance(p_left) < 50 and ball.xcor() < -360:
        ball.paddle_hit()
        hit_speed *= 1.5

    if ball.xcor() > 400:
        score.l_point()
        ball.refresh()

    if ball.xcor() < -400:
        score.r_point()
        ball.refresh()

    if score.l_score == 20 or score.r_score == 20:
        score.game_over()


screen.exitonclick()
