from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_Y_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def turtle_reached_end(self):
        return self.ycor() >= FINISH_Y_LINE

    def move(self, end=None):
        if self.turtle_reached_end():
            return
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)