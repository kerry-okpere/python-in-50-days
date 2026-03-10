from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.render_snake()
        self.head = self.segments[0]

    def render_snake(self):
        for position in STARTING_POS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # get the current position of each of the segments
        # move the first turtle to desired position
        # move the remiain turtle to the position in the next segment
        current_position = None
        for seg in self.segments:
            prev_positions = seg.pos()
            seg.penup()
            if seg == self.head:
                seg.forward(MOVE_DISTANCE)
                # seg.setheading(direction)
            else:
                seg.goto(current_position)

            current_position = prev_positions

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
