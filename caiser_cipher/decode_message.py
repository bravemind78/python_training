letter_list=["a", "b", "c", "d", "e", "f", "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def decode_message(message,shift_number):
    message_list=list(message)
    spaces_index_list=[]
    for index,letter in enumerate(message_list):
        if letter==" ":
            spaces_index_list.append(index)
    # print(message_list)
    # print(spaces_index_list)
    letter_index_list=[]
    for message_letter in message_list:
        for letter in letter_list:
            if message_letter==letter:
                letter_index_list.append(letter_list.index(letter))
    # print(letter_index_list)
    letter_index_shifted_list=[]
    for index in letter_index_list:
        new_index=index-shift_number
        if new_index<0:
            if shift_number>index+len(letter_list):
                new_index=((shift_number-index)%len(letter_list))*-1
            else:
                new_index=new_index
        else:
            new_index=new_index
        letter_index_shifted_list.append(new_index)
    # print(letter_index_shifted_list)
    shifted_letter_list=[]
    for index in letter_index_shifted_list:
        shifted_letter_list.append(letter_list[index])
    # print(shifted_letter_list)
    for space in spaces_index_list:
        shifted_letter_list.insert(space," ")
    # print(shifted_letter_list)
    decoding_message="".join(shifted_letter_list)
    print(f"here is the decoding message : {decoding_message}")
# message=input("Enter message : ")
# shift_number=int(input("Enter shifted number : "))
# decode_message(message,shift_number)
