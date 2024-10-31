from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x_cordinates):
        super().__init__()
        self.x_cordinates=x_cordinates
        self.creat_paddle()
# ---------------------------------------------------------------------------- #
# ----------------------------- Create The Paddle ---------------------------- #
    def creat_paddle(self):
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.speed(0.05)
        self.goto(self.x_cordinates,0)
# ---------------------------------------------------------------------------- #
# ---------------------------- Move the paddle up ---------------------------- #
    def move_up(self):
      current_ycor=self.ycor()
      new_ycor=current_ycor+80
      self.goto(self.x_cordinates,new_ycor)
# ---------------------------------------------------------------------------- #
# --------------------------- Move the paddle down --------------------------- #
    def move_down(self):
        current_ycor=self.ycor()
        new_ycor=current_ycor-80
        self.goto(self.x_cordinates,new_ycor)
# ---------------------------------------------------------------------------- #
# ------------------ Set the paddle to the original location ----------------- #
    def reset_location(self):
        self.goto(self.x_cordinates,0)
# ---------------------------------------------------------------------------- #