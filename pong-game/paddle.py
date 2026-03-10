from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, starting_pos):
        super().__init__()
        self.starting_pos = starting_pos
        self.render_paddle_new()
        
    def render_paddle_new(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.starting_pos)
        
    def up(self):
        if self.ycor() < 260:
            self.goto(self.starting_pos[0], self.ycor()+20)

    def down(self):
        if self.ycor() > -240:
            self.goto(self.starting_pos[0], self.ycor()-20)
