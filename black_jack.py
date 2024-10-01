import random
while True:
    play_game_decision=input("Do you Want to play Black Jack Game? (y/n): ")
    if(play_game_decision=="y"):
        user_choice1=random.randint(1,10)
        user_choice2=random.randint(1,10)
        computer_choice1=random.randint(1,10)
        user_choice_list=[user_choice1,user_choice2]
        if(user_choice1+user_choice2)==21:
            computer_choice2=random.randint(1,10)
            print(f"your cards: {user_choice_list} with score '21'")
            print(f"computer first choice is : {computer_choice1}")
            print(f"Now you are black Jack !")
            if (computer_choice1+computer_choice2)==21:
                computer_choice_list=[computer_choice1,computer_choice2]
                print(f"computer choices are {computer_choice_list} with score '21'")
                print("The game is Draw because you and computer are black jack")
            else:
                computer_choice_list=[computer_choice1,computer_choice2]
                print (f"computer choices are {computer_choice_list} with score {computer_choice1+computer_choice2}")
                print("congratulation you are win")
        else:
            print(f"your cards: {user_choice_list} with score {user_choice1+user_choice2}")
            print(f"computer first choice is : {computer_choice1}")
            while True:
                user_decision=input("type 'y' to get another card type 'n' to pass: ")
                if user_decision=="y":
                    user_choice3=random.randint(1,10)
                    user_choice_list.append(user_choice3)
                    user_list_sumtion=sum(user_choice_list)
                    if user_list_sumtion>21:
                        print(f"your cards: {user_choice_list} with score {user_list_sumtion}")
                        print("sorry you lose the game")
                        break
                    elif user_list_sumtion==21:
                        print(f"your cards: {user_choice_list} with score {user_list_sumtion}")
                        print("Bravo you got score '21'")
                        break
                    print(f"your cards: {user_choice_list} with score {user_list_sumtion}")
                    print(f"computer first choice is : {computer_choice1}")
                else:
                    break
            computer_choice2=random.randint(1,10)
            computer_choice_list=[computer_choice1,computer_choice2]
            computer_list_sum=sum(computer_choice_list)
            if user_list_sumtion>21:
                print("Game Over")
            else:
                while True:
                    if computer_list_sum<17:
                        computer_choice3=random.randint(1,10)
                        computer_choice_list.append(computer_choice3)
                        computer_list_sum=sum(computer_choice_list)
                    else:
                        break
                if computer_list_sum>21:
                    print(f"your cards: {user_choice_list} with score {user_list_sumtion}")
                    print (f"computer choices are {computer_choice_list} with score {computer_list_sum}")
                    print("congratulation you won the game ")
                elif computer_list_sum<user_list_sumtion:
                    print(f"your cards: {user_choice_list} with score {user_list_sumtion}")
                    print (f"computer choices are {computer_choice_list} with score {computer_list_sum}")
                    print("congratulation you won the game ")
                elif computer_list_sum>user_list_sumtion:
                    print(f"your cards: {user_choice_list} with score {user_list_sumtion}")
                    print (f"computer choices are {computer_choice_list} with score {computer_list_sum}")
                    print("Sorry You Lose The Game")
                elif computer_list_sum==user_list_sumtion:
                    print(f"your cards: {user_choice_list} with score {user_list_sumtion}")
                    print (f"computer choices are {computer_choice_list} with score {computer_list_sum}")
                    print("Game is Draw")
    else:
        break