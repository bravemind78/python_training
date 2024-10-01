#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list=[]
for i in range(0,nr_letters):
    letters_index=random.randint(0, nr_letters-1)
    password_list.append(letters[letters_index])
for i in range(0,nr_symbols):
    symbols_index=random.randint(0, nr_symbols-1)
    password_list.append(symbols[symbols_index])
for i in range (0,nr_numbers):
    number_index=random.randint(0,nr_numbers-1)
    password_list.append(numbers[number_index])
final_password_list=[]
for element in password_list:
    final_index=random.randint(0,len(password_list)-1)
    final_password_list.append(password_list[final_index])

final_password="".join(final_password_list)
print(f"Your Strong Passwprd is : {final_password}")


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P