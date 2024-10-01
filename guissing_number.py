import random
# ---------------------------------------------------------------------------- #
#                             Variables Definitions                            #
# ---------------------------------------------------------------------------- #
guess_number_logo="""
   ___                                      __                    _
  / _ \ _   _   ___  ___  ___    __ _    /\ \ \ _   _  _ __ ___  | |__    ___  _ __
 / /_\/| | | | / _ \/ __|/ __|  / _` |  /  \/ /| | | || '_ ` _ \ | '_ \  / _ \| '__|
/ /_\\ | |_| ||  __/\__ \\__ \ | (_| | / /\  / | |_| || | | | | || |_) ||  __/| |
\____/  \__,_| \___||___/|___/  \__,_| \_\ \/   \__,_||_| |_| |_||_.__/  \___||_|
"""
# ---------------------------------------------------------------------------- #
#                             Function Definitions                             #
# ---------------------------------------------------------------------------- #
# -------------------- it is function to guess the number -------------------- #
def guess_number(computer_guessing_number,number_of_try):
            while number_of_try>0:
                user_guess=int(input("Make a Guess: "))
                if user_guess<computer_guessing_number:
                    print("it is too Low")
                    number_of_try-=1
                elif user_guess>computer_guessing_number:
                    print(" it is too High")
                    number_of_try-=1
                elif user_guess==computer_guessing_number:
                    print(f"Congratulation you won the game the number is : {computer_guessing_number}")
                    break
            if number_of_try==0:
                print("sorry you have attemped all of your guess, Game is over")
    # ---------------------------------------------------------------------------- #
while True:
    print(guess_number_logo)
    play_or_not=input("do you want to play Gussing number? (y/n):")
    if  play_or_not=="y":
        computer_guessing_number=random.randint(1,100)
        number_of_try=0
        difficulty=input("choose a difficulity type 'easy' or 'hard'")
        if difficulty=='easy':
            number_of_try=10
        else:
            number_of_try=5
        print(f"you have {number_of_try} remaining to guess the number")
        guess_number(computer_guessing_number,number_of_try)
    else:
        break