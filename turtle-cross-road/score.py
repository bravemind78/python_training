from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self,level):
        super().__init__()
        self.level=level
        self.create_board()
# ---------------------------------------------------------------------------- #
    def create_board(self):
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-250,250)
        self.write(f"Level : {self.level}", font=('Arial', 24, 'normal'))
# ---------------------------------------------------------------------------- #
    def update_board(self):
        self.clear()
        self.level+=1
        self.create_board()
# ----------------------------------------------------------------------------
    def game_over(self):
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-100,0)
        self.write("Game Over", font=('Arial', 32, 'normal'))
# ---------------------------------------------------------------------------- #