from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle((-350, 0))
player2 = Paddle((350, 0))
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.go_up, "w")
screen.onkey(player1.go_down, "s")
screen.onkey(player2.go_up, "Up")
screen.onkey(player2.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.xcor() < -320 and ball.distance(player1) < 55) \
            or ball.xcor() > 320 and ball.distance(player2) < 55:
        ball.bounce_x()

    # detect player1 misses
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.player2_point()

    # detect player2 misses
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.player1_point()

screen.exitonclick()
