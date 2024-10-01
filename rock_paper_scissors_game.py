import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_choice=int(input("Enter 0 for rock, 1 for Scissors and 2 for paper : "))
computer_choice=random.randint(0,2)
if user_choice==0:
    print(rock)
    if computer_choice==0:
        print(rock)
        print("Game Draw")
    elif computer_choice==1:
        print(Scissors)
        print("Congratulations you have won!")
    elif computer_choice==2:
        print(paper)
        print("Sorry you lose the Game!")
elif user_choice==1:
    print(Scissors)
    if computer_choice==0:
        print(rock)
        print("Sorry you lose the Game!")
    elif computer_choice==1:
        print(Scissors)
        print("Game Draw")
    elif computer_choice==2:
        print(paper)
        print("Congratulations you have won!")
elif user_choice==2:
    print(paper)
    if computer_choice==0:
        print(rock)
        print("Congratulations you have won!")
    elif computer_choice==1:
        print(Scissors)
        print("Sorry you lose the Game!")
    elif computer_choice==2:
        print(paper)
        print("Game Draw")
else:
    print("you choice wrong number,please try again")