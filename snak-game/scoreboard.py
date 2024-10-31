from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.create_score_board()
# ---------------------------------------------------------------------------- #
    def create_score_board(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.write("score is 0 ", align="center", font=("Arial", 16, "bold"))
# ---------------------------------------------------------------------------- #
    def show_score(self,new_score):
        self.clear()
        self.write(f"score is {new_score}", align="center", font=("Arial", 16, "bold"))