def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
calculator_logo="""
 _______  _______  _        _______           _        _______ _________ _______  _______
(  ____ \(  ___  )( \      (  ____ \|\     /|( \      (  ___  )\__   __/(  ___  )(  ____ )
| (    \/| (   ) || (      | (    \/| )   ( || (      | (   ) |   ) (   | (   ) || (    )|
| |      | (___) || |      | |      | |   | || |      | (___) |   | |   | |   | || (____)|
| |      |  ___  || |      | |      | |   | || |      |  ___  |   | |   | |   | ||     __)
| |      | (   ) || |      | |      | |   | || |      | (   ) |   | |   | |   | || (\ (
| (____/\| )   ( || (____/\| (____/\| (___) || (____/\| )   ( |   | |   | (___) || ) \ \__
(_______/|/     \|(_______/(_______/(_______)(_______/|/     \|   )_(   (_______)|/   \__/
"""
while True:
    print(calculator_logo)
    first_number=float(input("what is the first number: "))
    comulative_number=0
    while True:
        print("+\n-\n*\n/")
        operation=input("pick an operation : ")
        if operation=="+":
            second_number=float(input("what is the next number: "))
            result=add(first_number,second_number)
            comulative_number=result
            print(f"{first_number}+{second_number}={comulative_number}")
            first_number=comulative_number
        elif operation=="-":
            second_number=float(input("what is the next number: "))
            result=subtract(first_number,second_number)
            comulative_number=result
            print(f"{first_number}-{second_number}={comulative_number}")
            first_number=comulative_number
        elif operation=="*":
            second_number=float(input("what is the next number: "))
            result=multiply(first_number,second_number)
            comulative_number=result
            print(f"{first_number}*{second_number}={comulative_number}")
            first_number=comulative_number
        elif operation=="/":
            second_number=float(input("what is the next number: "))
            result = divide(first_number,second_number)
            comulative_number=result
            print(f"{first_number}/{second_number}={comulative_number}")
            first_number=comulative_number
        else:
            print("you choose nothing,please try again")
        end_caculation=input(f"type 'y' to continue caculating with {comulative_number} or type 'n' to start new calculation !")
        if end_caculation=="n":
            comulative_number=0
            break