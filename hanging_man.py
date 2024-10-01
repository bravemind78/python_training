import random
hang_man_pic = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
player_one_word=input("player one please input your guess word: ")
player_one_word_letter_list=list(player_one_word)
result_word_letter_list=[]
for letter in player_one_word_letter_list:
    result_word_letter_list+="-"
print (f"player two you hanve a word with {len(player_one_word_letter_list)} letters ")
hang_man_pic_index=0
while player_one_word_letter_list!=result_word_letter_list: 
    player_two_guess_letter=input ("please input your guess letter: ")
    if player_two_guess_letter in player_one_word_letter_list:
        for index,letter in enumerate(player_one_word_letter_list):
            if letter==player_two_guess_letter:
                result_word_letter_list[index]=letter
        print("".join(result_word_letter_list))
    else:
        print(hang_man_pic[hang_man_pic_index])
        hang_man_pic_index+=1
        print(hang_man_pic_index)
        if hang_man_pic_index >(len(hang_man_pic)-1):
            break
if hang_man_pic_index>6:
    print("sorry game over")
else:
    print("you are win")