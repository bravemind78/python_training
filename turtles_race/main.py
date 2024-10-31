from turtle import Turtle,Screen
from tkinter import messagebox
import random
screen=Screen()
screen.setup(width=500,height=400)
user_choice=screen.textinput(title="Enter your Bid",prompt="which turtle will win the race, Enter your Color: ")
turtles_color=[ "red", "orange", "yellow", "green", "blue", "violet"]
# ---------------------- Function to generate 6 turtles ---------------------- #
def generate_turtles():
    turtles_objects=[]
    for i in range(0,6):
        tim=Turtle()
        turtles_objects.append(tim)
    return turtles_objects
# ---------------------------------------------------------------------------- #
# ----------------- Function to move turtules to start point ----------------- #
def start_point():
    index=0
    distance=-40
    for turtle in turtules_objects:
        turtle.shape("turtle")
        turtle.color(turtles_color[index])
        index+=1
        turtle.penup()
        turtle.goto(-230,distance)
        distance+=40
# ---------------------------------------------------------------------------- #
def add_comulative_steps():
    for turtle in turtules_objects:
        turtle.commulated_steps=0
# ---------------------------------------------------------------------------- #
def move_forward():
    add_comulative_steps()
    keep_running=True
    while keep_running:
        for turtle in turtules_objects:
            step=random.randint(0,10)
            turtle.forward(step)
            turtle.commulated_steps+=step
            if turtle.commulated_steps>480:
                keep_running=False
                return turtle
# ---------------------------------------------------------------------------- #
turtules_objects=generate_turtles()
start_point()
wining_turtle=move_forward()
if wining_turtle.color()[0]==user_choice:
    print("congratulation you are win")
    messagebox.showinfo("race result",f"the winning turtle is {wining_turtle.color()[0]} congratulation we have a winner!")
else:
    print("Hard Luck You are Loser")
    messagebox.showinfo("race result",f"the winning turtle is {wining_turtle.color()[0]}, Hard Luck You are Loser !")






screen.exitonclick()