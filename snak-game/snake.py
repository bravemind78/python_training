from turtle import Turtle
class Snake:
# ---------------------------------------------------------------------------- #
# -------------------------- Initialize snake class -------------------------- #
    def __init__(self,create_snake=True):
        self.snake_parts=[]
        if create_snake:
            self.create_snake()
        self.north_south_d=True
        self.east_west_d=True
# ---------------------------------------------------------------------------- #
# -------------------------------- Creat Snake ------------------------------- #
    def create_snake(self):
        for i in range(0,3):
            jemy=Turtle()
            jemy.color("white")
            jemy.shape("square")
            self.snake_parts.append(jemy)
        index=0
        for snake_part in self.snake_parts:
            snake_part.penup()
            snake_part.goto(index,0)
            index-=20
# ---------------------------------------------------------------------------- #
# ------------------------------ Move The Snake ------------------------------ #
    def move_snake(self):
        current_coordinates=[]
        for snake_part in self.snake_parts:
            current_x_cor=snake_part.xcor()
            current_y_cor=snake_part.ycor()
            current_location=(current_x_cor,current_y_cor)
            current_coordinates.append(current_location)
        self.snake_parts[0].forward(20)
        head_x=self.snake_parts[0].xcor()
        head_y=self.snake_parts[0].ycor()
        head_cordinates=[head_x,head_y]
        for i in range(len(self.snake_parts)-1,0,-1):
            self.snake_parts[i].goto(current_coordinates[i-1])
        return head_cordinates
# ---------------------------------------------------------------------------- #
# ----------------------------- Turn the snake Up ---------------------------- #
    def turn_north(self):
        if self.north_south_d:
            self.snake_parts[0].setheading(90)
            self.north_south_d=False
            self.east_west_d=True
# ---------------------------------------------------------------------------- #
# ---------------------------- Turn the snake Down --------------------------- #
    def turn_south(self):
        if self.north_south_d:
            self.snake_parts[0].setheading(270)
            self.north_south_d=False
            self.east_west_d=True
# ---------------------------------------------------------------------------- #
# --------------------------- Tuen the snake Right --------------------------- #
    def turn_east(self):
        if self.east_west_d:
            self.snake_parts[0].setheading(0)
            self.north_south_d=True
            self.east_west_d=False
# ---------------------------------------------------------------------------- #
# ---------------------------- Turn The Snake Left --------------------------- #
    def turn_west(self):
        if self.east_west_d:
            self.snake_parts[0].setheading(180)
            self.north_south_d=True
            self.east_west_d=False
# ---------------------------------------------------------------------------- #
# -------------------- Add Part To Snake when hit the ball ------------------- #
    def add_body_part(self):
        jemy=Turtle()
        jemy.color("white")
        jemy.shape("square")
        jemy.penup()
        self.snake_parts.append(jemy)
# ---------------------------------------------------------------------------- #
# ------------------------ Check Clollision with tail ------------------------ #
    # def check_tail_collision(self):
    #     i=1
    #     for i in range(i,len(self.snake_parts)):
    #         if abs(self.snake_parts[0].xcor()-self.snake_parts[i].xcor())<18 and abs(self.snake_parts[0].ycor()-self.snake_parts[i].ycor())<18:
    #             return True
# ---------------------------------------------------------------------------- #
    def check_tail_collision(self):
        snake_head=self.snake_parts[0]
        for part in self.snake_parts[1:]:
            if abs(snake_head.xcor()-part.xcor())<18 and abs(snake_head.ycor()-part.ycor())<18:
                return True