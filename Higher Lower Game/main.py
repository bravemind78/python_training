import data_source
import logos
import random
data_list=data_source.data
current_score=0
def select_character():
    random_index=random.randint(0,(len(data_list)-1))
    name=data_list[random_index]["name"]
    title=data_list[random_index]["title"]
    country=data_list[random_index]["country"]
    followers=data_list[random_index]["followers"]
    return [f"{name} , {title}, from {country}",followers]
def check_dublicate(charcter_a, character_b):
    while True:
        if charcter_a[0]==character_b[0]:
            character_b=select_character()
        else:
            break
    return character_b

character_a=select_character()
character_b=select_character()
character_b=check_dublicate(character_a,character_b)
while True:
    print(logos.higher_lower_logo)
    print(f"You are Right ,current score is :{current_score}")
    print(f"Compare A: {character_a[0]}")
    print(logos.versus_logo)
    print(f"Against B : {character_b[0]}")
    user_choice=(input("who has more followers?Type 'A' or 'B':  ")).lower()
    print("\n"*100)
    if user_choice=="a":
        if character_a[1]>character_b[1]:
            current_score+=1
            character_a=character_b
            character_b=select_character()
            character_b=check_dublicate(character_a,character_b)
        else:
            print(logos.higher_lower_logo)
            print(f"Sorry, that's wrong. Final score is {current_score}")
            break
    elif user_choice=="b":
        if character_a[1]<character_b[1]:
            current_score+=1
            character_a=character_b
            character_b=select_character()
            character_b=check_dublicate(character_a,character_b)
        else:
            print(logos.higher_lower_logo)
            print(f"Sorry, that's wrong. Final score is {current_score}")
            break