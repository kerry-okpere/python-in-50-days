from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# Steps
# use a turtle to wite a dashed line across the Y axis and store it from moving and hide it 
# use turtle(dynamic) to draw a number 
# use turtle(1) to draw the ball
# use turtle(4) to draw the two paddle
# When the ball hits a turtle calculate the degree path the ball should travel on 

# Based on lesson 
# create screen
# create paddle and move paddle 
# create another paddle 
# create ball and make it move 
# Detect wall collision and bounce ball
# Detect paddle collision
# keep score 
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")
speed = 1

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.y_bounce()

    if (ball.distance(paddle1) < 50 and ball.xcor() > 320) or (ball.distance(paddle2) < 50 and ball.xcor() < -320):
       ball.x_bounce()
       speed = speed * 0.9

    if (ball.xcor() > 380):
        scoreboard.l_point()
        ball.reset_pos()
        speed = 1

    if (ball.xcor() < -380):
        scoreboard.r_point()
        ball.reset_pos()
        speed = 1
    



screen.exitonclick()
