from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.listen()
snake=Snake()
screen.update()
game_on=True
food=Food()
new_score=0
score_board=ScoreBoard()
def keyboard_controller():
    screen.onkey(snake.turn_north,"Up")
    screen.onkey(snake.turn_east,"Right")
    screen.onkey(snake.turn_west,"Left")
    screen.onkey(snake.turn_south,"Down")
food_point=food.create_food()
screen.update()
while game_on:
    keyboard_controller()
    head_point=snake.move_snake()
    collision=snake.check_tail_collision()
    if collision:
        game_on=False
        print(collision)
        screen.update()
    screen.update()
    time.sleep(0.15)
    if abs(head_point[0] - food_point[0]) < 20 and abs(head_point[1] - food_point[1]) < 20:
        food_point=food.create_food()
        new_score+=1
        score_board.show_score(new_score)
        snake.add_body_part()
        screen.update()
    if (screen.window_width()/2)-head_point[0] <=0 or (screen.window_width()/2)-head_point[0]>=600:
        game_on=False
        screen.update()
    if (screen.window_height()/2)-head_point[1] <=0 or (screen.window_height()/2)-head_point[1]>=600:
        game_on=False
        screen.update()
game_over=Turtle()
game_over.hideturtle()
game_over.penup()
game_over.goto(0,0)
game_over.color("white")
game_over.write("Game Over",align="center", font=("Arial", 16, "bold"))
screen.update()

























screen.exitonclick()