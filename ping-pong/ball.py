from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_increment=10
        self.y_increment=10
        self.time_sleep=0.1
        self.create_ball()
# ---------------------------------------------------------------------------- #
    def create_ball(self):
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0,0)
# ---------------------------------------------------------------------------- #
    def move_ball(self):
        x=self.xcor()
        y=self.ycor()
        self.goto(x+ self.x_increment,y+self.y_increment)
# ---------------------------------------------------------------------------- #
    def ball_bouncing_yaxis(self):
        if abs (300-self.ycor())<=10 or abs(300+self.ycor())<=10:
            self.y_increment=self.y_increment*-1
# ---------------------------------------------------------------------------- #
    def ball_bouncing_xaxis(self):
            self.x_increment=self.x_increment*-1
            self.time_sleep=self.time_sleep*0.95
# ---------------------------------------------------------------------------- #
