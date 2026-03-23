from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("crossing game")


player = Player()
scorecard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_turtle()
    car_manager.move()

    for car in car_manager.segments:
        if car.distance(player) < 20:
            scorecard.game_over()
            game_on = False

    if player.turtle_reached_end(): 
        scorecard.record_point()
        player.reset_position()
        car_manager.increase_speed()



screen.exitonclick()