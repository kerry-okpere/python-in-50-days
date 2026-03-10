from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")
timmy.color("coral")
colors = ['red', 'blue', 'green', 'pink', 'yellow']
counter = 4
max = 10

while counter <= max:
    for _ in range(counter):
        timmy.forward(100)
        timmy.left(360 / counter)
    counter = counter + 1
    timmy.color(random.choice(colors))


screen = Screen()
screen.exitonclick()
