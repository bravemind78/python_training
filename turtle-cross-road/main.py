from turtle import Screen
from player import Player 
from car import Car
from score import ScoreBoard
import time
import random
screen=Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on=True

# -------------------------- create a turtle player -------------------------- #
player=Player()
# ---------------------------------------------------------------------------- #
# ---------------------------- create score board ---------------------------- #
score_board=ScoreBoard(1)
# ---------------------------------------------------------------------------- #
# ------------------- create control function for up arrow ------------------- #
def key_controller():
    screen.onkey(player.move_turtle_forward,"Up")
# ---------------------------------------------------------------------------- #
screen.listen()
key_controller()
cars=[]
game_speed=0.25
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    if random.randint(1,6)==1:
        y_cord=random.randint(-250,250)
        color_index=random.randint(0,5)
        car=Car(y_cord,color_index)
        cars.append(car)
    for car in cars:
        car.move_car()
        if abs(car.xcor()-player.xcor())<20 and abs(car.ycor()-player.ycor())<20:
            score_board.game_over()
            game_is_on=False
        if player.ycor()>300:
            player.goto(0,-280)
            score_board.update_board()
            game_speed=game_speed*0.75


screen.exitonclick()