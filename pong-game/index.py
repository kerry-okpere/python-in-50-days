from turtle import Screen, Turtle
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
from paddle import Paddle
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
