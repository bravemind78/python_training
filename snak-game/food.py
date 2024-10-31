from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()
# ---------------------------------------------------------------------------- #
    def create_food(self):
        self.shape("circle")
        self.shapesize(0.8)
        self.color("blue")
        self.penup()
        x_cord=random.randint(-290,290)
        y_cord=random.randint(-290,290)
        self.goto(x_cord,y_cord)
        food_point=[x_cord,y_cord]
        return food_point