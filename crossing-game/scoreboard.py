from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-240, 240)
        self.write(f"Level {self.level}", font=FONT)

    def record_point(self):
        self.clear()
        self.level = self.level + 1
        self.write(f"Level {self.level}", font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font=FONT)
