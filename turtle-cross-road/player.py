from turtle import Turtle
class Player(Turtle):
    def __init__(self) :
        super().__init__()
        self.create_player()
# ---------------------------------------------------------------------------- #
# --------------------------- Create turtle player --------------------------- #
    def create_player(self):
        self.shape("turtle")
        self.speed(10)
        self.setheading(90)
        self.penup()
        self.goto(0,-280)
# ---------------------------------------------------------------------------- #
# ------------------- Move the turtle forward with step 10 ------------------- #
    def move_turtle_forward(self):
        self.forward(10)
# ---------------------------------------------------------------------------- #