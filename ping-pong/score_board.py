from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self,x_cor):
        super().__init__()
        self.score=0
        self.x_cor=x_cor
        self.create_score()
# ---------------------------------------------------------------------------- #
    def change_score(self):
        self.score+=1
        self.clear()  # مسح النتيجة القديمة
        self.create_score()  # إعادة كتابة النتيجة الجديدة
# ---------------------------------------------------------------------------- #
    def create_score(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(self.x_cor,230)
        self.write(self.score, font=('Arial', 40, 'normal'))
# ---------------------------------------------------------------------------- #