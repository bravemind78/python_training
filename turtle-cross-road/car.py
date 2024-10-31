from turtle import Turtle
class Car(Turtle):
    def __init__(self,y_cord,index):
        super().__init__()
        self.index=index
        self.car_colors=["red", "green", "orange", "yellow","purple","blue"]
        self.y_cord=y_cord
        self.create_car()
# ---------------------------------------------------------------------------- #
    def create_car(self):
        self.penup()
        self.shape("square")
        self.shapesize(1,2)
        self.color(self.car_colors[self.index])
        self.goto(250,self.y_cord)
# ---------------------------------------------------------------------------- #
    def move_car(self):
        self.backward(10)
# ---------------------------------------------------------------------------- #