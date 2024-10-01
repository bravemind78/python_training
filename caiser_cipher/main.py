import encode_message
import decode_message
cypher="""
        CCCCCCCCCCCCC  iiii                      hhhhhhh
     CCC::::::::::::C i::::i                     h:::::h
   CC:::::::::::::::C  iiii                      h:::::h
  C:::::CCCCCCCC::::C                            h:::::h
 C:::::C       CCCCCCiiiiiii ppppp   ppppppppp    h::::h hhhhh           eeeeeeeeeeee    rrrrr   rrrrrrrrr
C:::::C              i:::::i p::::ppp:::::::::p   h::::hh:::::hhh      ee::::::::::::ee  r::::rrr:::::::::r
C:::::C               i::::i p:::::::::::::::::p  h::::::::::::::hh   e::::::eeeee:::::eer:::::::::::::::::r
C:::::C               i::::i pp::::::ppppp::::::p h:::::::hhh::::::h e::::::e     e:::::err::::::rrrrr::::::r
C:::::C               i::::i  p:::::p     p:::::p h::::::h   h::::::he:::::::eeeee::::::e r:::::r     r:::::r
C:::::C               i::::i  p:::::p     p:::::p h:::::h     h:::::he:::::::::::::::::e  r:::::r     rrrrrrr
C:::::C               i::::i  p:::::p     p:::::p h:::::h     h:::::he::::::eeeeeeeeeee   r:::::r
 C:::::C       CCCCCC i::::i  p:::::p    p::::::p h:::::h     h:::::he:::::::e            r:::::r
  C:::::CCCCCCCC::::Ci::::::i p:::::ppppp:::::::p h:::::h     h:::::he::::::::e           r:::::r
   CC:::::::::::::::Ci::::::i p::::::::::::::::p  h:::::h     h:::::h e::::::::eeeeeeee   r:::::r
     CCC::::::::::::Ci::::::i p::::::::::::::pp   h:::::h     h:::::h  ee:::::::::::::e   r:::::r
        CCCCCCCCCCCCCiiiiiiii p::::::pppppppp     hhhhhhh     hhhhhhh    eeeeeeeeeeeeee   rrrrrrr
                              p:::::p
                              p:::::p
                             p:::::::p
                             p:::::::p
                             p:::::::p
                             ppppppppp

"""
status=True
while status==True:
    print(cypher)
    user_choice=input("Type 'encode' to encrypt ,type 'decode' to decrypt:\n")
    if user_choice == 'encode':
        message=input("Type your message to encrypt : \n")
        shift_number=int(input("type the shift number: \n"))
        encode_message.encode_message(message,shift_number)
    elif user_choice == 'decode':
        message=input("Type your message to decrypt : \n")
        shift_number=int(input("type the shift number: \n"))
        decode_message.decode_message(message,shift_number)
    else:
        print("you didn't choice anything")
    contineu_programe=input("Type 'yes' if you want to go again , otherwise type 'no'.")
    if contineu_programe == "no":
        break