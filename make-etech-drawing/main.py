from turtle import Turtle,Screen
# ---------------------------------------------------------------------------- #
def move_forward():
    timmy.forward(10)
# ---------------------------------------------------------------------------- #
def move_backward():
    timmy.backward(10)
# ---------------------------------------------------------------------------- #
def counter_clockwise():
    timmy.left(10)
# ---------------------------------------------------------------------------- #
def clockwise():
    timmy.right(10)
# ---------------------------------------------------------------------------- #
def draw_curve():
    timmy.circle(100,30)
# ---------------------------------------------------------------------------- #
def clear_screen():
    timmy.clear()
    timmy.home()
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
def control_keys():
    screen.onkey(move_forward,"w")
    screen.onkey(move_backward,"s")
    screen.onkey(counter_clockwise,"a")
    screen.onkey(clockwise,"c")
    screen.onkey(draw_curve,"Up")
    screen.onkey(clear_screen,"x")
# ---------------------------------------------------------------------------- #

timmy=Turtle()
screen=Screen()
control_keys()
screen.listen()
screen.exitonclick()