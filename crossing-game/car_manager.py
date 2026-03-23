import random
from turtle import Turtle

COLOR = ["red", "blue", "green", "yellow", "purple", "orange"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_AXIS = [-250, -220, -190, -160, -130, -100, -70, -40, -10, 20, 50, 80, 110, 140, 170, 200, 230, 260]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.segments: list[Turtle] = []
        self.move_by = STARTING_MOVE_DISTANCE

    def create_turtle(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            turtle = Turtle()
            turtle.shape('square')
            turtle.penup()
            turtle.color(random.choice(COLOR))
            turtle.shapesize(stretch_wid=1, stretch_len=3)
            turtle.goto(320, random.randint(-230, 250))
            self.segments.append(turtle)

    def move(self):
        for index, turtle in enumerate(self.segments):
            turtle.forward(-self.move_by)


    def increase_speed(self):
        self.move_by = self.move_by + MOVE_INCREMENT


