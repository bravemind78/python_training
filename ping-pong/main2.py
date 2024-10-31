from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

# ---------------------------------------------------------------------------- #
# ------------------------------- Screen Screen ------------------------------ #
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

# ---------------------------------------------------------------------------- #
# ------------------------------ create a paddle ----------------------------- #
paddle = Paddle(380)
paddle2 = Paddle(-390)

# ---------------------------------------------------------------------------- #
# ------------------------------- Create a Ball ------------------------------ #
ball = Ball()

# ---------------------------------------------------------------------------- #
# ------------------------ Create Score for paddle one ----------------------- #
score_player1 = ScoreBoard(75)
score_player2 = ScoreBoard(-75)

# ---------------------------------------------------------------------------- #
isgame = True
# time_sleep = 0.1

# ---------------------------------------------------------------------------- #
#                             FUNCTION DEFINITIONS                             #
# ---------------------------------------------------------------------------- #
final_score = screen.numinput("final points", "Enter your final winning points:", 6, minval=3, maxval=10)

# تأكد من أن final_score ليست None
if final_score is not None:
    final_score = int(final_score)
else:
    final_score = 6  # قيمة افتراضية في حال إغلاق المستخدم للصندوق

# ------------------------- KEY CONTROL IN PADDLES ------------------------- #
def controller_keys():
    screen.onkey(paddle.move_up, "Up")
    screen.onkey(paddle.move_down, "Down")
    screen.onkey(paddle2.move_up, "w")
    screen.onkey(paddle2.move_down, "s")
    screen.onkey(paddle.reset_location, "h")
    screen.onkey(paddle2.reset_location, "j")

# ---------------------------------------------------------------------------- #
# ------------------------ collision ball with paddles ----------------------- #
def ball_paddles_collision():
    if (ball.distance(paddle) <= 50 and ball.xcor() > 360) or (ball.distance(paddle2) <= 50 and ball.xcor() < -360):
        ball.ball_bouncing_xaxis()

# ---------------------------------------------------------------------------- #
# ------------------------- collision ball with walls ------------------------ #
def ball_goes_outboarders():
    if ball.xcor() > 380:
        ball.home()
        score_player2.change_score()
        screen.update()
    elif ball.xcor() < -380:
        ball.home()
        score_player1.change_score()
        screen.update()

# ---------------------------------------------------------------------------- #
controller_keys()
screen.listen()  # يجب أن يتم استدعاء listen بعد إعداد التحكم

wining_player = ""

while isgame:
    ball.move_ball()
    ball.ball_bouncing_yaxis()
    ball_paddles_collision()
    ball_goes_outboarders()
    screen.update()
    time.sleep(ball.time_sleep)  # استخدم time_sleep مباشرة

screen.exitonclick()