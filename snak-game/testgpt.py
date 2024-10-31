from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# ---------------------------------------------------------------------------- #
def create_snake_parts():
    snake_parts = []
    for i in range(0, 3):
        jemy = Turtle()
        jemy.color("white")
        jemy.shape("square")
        snake_parts.append(jemy)
    return snake_parts

# ---------------------------------------------------------------------------- #
def show_snake_body():
    snake_parts = create_snake_parts()
    i = 0
    for snakepart in snake_parts:
        snakepart.penup()
        snakepart.goto(i, 0)
        i -= 20
    screen.update()
    return snake_parts

# ---------------------------------------------------------------------------- #
def move_snake_forward(snake_parts):
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        last_positions = []
        for part in snake_parts:
            x = part.xcor()  # الحصول على إحداثيات x
            y = part.ycor()  # الحصول على إحداثيات y
            last_positions.append((x, y))  # إضافة الإحداثيات إلى القائمة
        snake_parts[0].forward(20)
        for i in range(len(snake_parts)-1, 0, -1):
            new_x = last_positions[i-1][0]
            new_y = last_positions[i-1][1]
            snake_parts[i].goto(new_x, new_y)
        screen.update()

# ---------------------------------------------------------------------------- #
def turn_snake_north():
    snake_parts[0].setheading(90)

# ---------------------------------------------------------------------------- #
def turn_snake_east():
    snake_parts[0].setheading(0)

# ---------------------------------------------------------------------------- #
def turn_snake_west():
    snake_parts[0].setheading(180)

# ---------------------------------------------------------------------------- #
def turn_snake_south():
    snake_parts[0].setheading(270)

# ---------------------------------------------------------------------------- #
snake_parts = show_snake_body()

# Event listeners for keypresses
screen.listen()
screen.onkey(lambda: turn_snake_north(), "Up")
screen.onkey(lambda: turn_snake_east(), "Right")
screen.onkey(lambda: turn_snake_west(), "Left")
screen.onkey(lambda: turn_snake_south(), "Down")

# Start moving the snake forward
move_snake_forward(snake_parts)

screen.mainloop()
