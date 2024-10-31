# import colorgram
# colors = colorgram.extract('hiris.jpg', 34)
# rgb_colors=[]
# for object in colors:
#     actual_color_r=object.rgb.r
#     actual_color_g=object.rgb.g
#     actual_color_b=object.rgb.b
#     actual_color=(actual_color_r,actual_color_b,actual_color_g)
#     rgb_colors.append(actual_color)
# print(rgb_colors)
# print(len(rgb_colors))
from turtle import Turtle,Screen
import random
colors_list=[(207, 82, 159), (54, 130, 89), (146, 39, 91), (140, 48, 26), (222, 107, 206), (132, 203, 177), (158, 83, 46), (45, 104, 55), (170, 39, 160), (129, 143, 189), (83, 44, 20), (37, 69, 43), (186, 106, 94), (185, 172, 140), (84, 180, 120), (59, 31, 39), (87, 91, 157), (78, 164, 153), (195, 72, 78), (161, 219, 201), (80, 44, 74), (45, 77, 74), (57, 124, 128), (218, 187, 176), (168, 169, 207), (220, 169, 181), (179, 211, 188), (47, 72, 73), (150, 35, 37), (44, 62, 63)]
jemmy=Turtle()
jemmy.hideturtle()
jemmy.speed(400)
screen=Screen()
screen.colormode(255)
direc=True
# ---------------------------------------------------------------------------- #
def draw_first_line():
    for i in range(10):
        index=random.randint(0,len(colors_list)-1)
        jemmy.dot(35,colors_list[index])
        jemmy.penup()
        jemmy.forward(68)
        jemmy.pendown()
# ---------------------------------------------------------------------------- #
def turn_left():
    jemmy.left(90)
    jemmy.penup()
    jemmy.forward(68)
    jemmy.left(90)
# ---------------------------------------------------------------------------- #
def turn_right():
    jemmy.right(90)
    jemmy.penup()
    jemmy.forward(68)
    jemmy.right(90)
# ---------------------------------------------------------------------------- #
def direction(direc):
    if direc:
        return turn_right() 
    else:
        return turn_left()
# ---------------------------------------------------------------------------- #
def draw_second_row_set():
    global direc
    for _ in range(8):
        draw_first_line()
        direction(direc)
        jemmy.forward(68)
        direc = not direc
# ---------------------------------------------------------------------------- #
jemmy.penup()
jemmy.goto(-300,300)
jemmy.pendown()
draw_second_row_set()
screen.exitonclick()
