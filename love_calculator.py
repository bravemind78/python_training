
def love_calculation(your_name,partner_name):
    your_name_list=list(your_name)
    partner_name_list=list(partner_name)
    total_list=your_name_list+partner_name_list
    true_list=["t","r","u","e"]
    love_list=["l","o","v","e"]
    true_index=0
    love_index=0
    for true_letter in true_list:
        for letter in total_list:
            if true_letter == letter:
                true_index+=1
    for love_letter in love_list:
        for letter in total_list:
            if love_letter == letter:
                love_index+=1
    love_score=(true_index*10)+1
    print(f"your Love Score is {love_score}%")
your_name=input("kindly Enter your Name:  ")
partner_name=input("kindly Enter your partner Name:  ")
love_calculation(your_name,partner_name)