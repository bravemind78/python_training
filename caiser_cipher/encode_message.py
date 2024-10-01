letter_list=["a", "b", "c", "d", "e", "f", "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encode_message(message,shift_number):
     message_list=list(message)
     spaces_index_list=[]
     for index,letter in enumerate (message_list):
         if letter==' ':
             spaces_index_list.append(index)
    #  print(spaces_index_list)
     letter_index_list=[]
     for message_letter in message_list:
         for letter in letter_list:
             if letter==message_letter:
                 letter_index=letter_list.index(letter)
                 letter_index_list.append(letter_index)
     shifted_letter_index_list=[]
     for number in letter_index_list:
         new_index=number+shift_number
         if (new_index-(len(letter_list)-1))>0:
            #  new_index=(new_index-(len(letter_list)-1))-1
            new_index=(new_index%(len(letter_list)))
         else:
             new_index=new_index
         shifted_letter_index_list.append(new_index)
    #  print(letter_index_list)
    #  print(shifted_letter_index_list)
     shifted_message_list=[]
     for index in shifted_letter_index_list:
         shifted_message_list.append(letter_list[index])
    #  print(shifted_message_list)
     for space in spaces_index_list:
        shifted_message_list.insert(space, ' ')
    #  print(shifted_message_list)
     encoded_message="".join(shifted_message_list)
     print(f"here is the encoded result: {encoded_message}")
# message=input("Type your message:  ")
# shift_number=int(input("Type the shift Number: "))
# encode_message(message,shift_number)