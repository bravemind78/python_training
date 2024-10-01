import data
# ---------------------------------------------------------------------------- #
#                             Variables Defintions                             #
# ---------------------------------------------------------------------------- #
# ---------------------------- modules Defintions ---------------------------- #
menu=data.menu
resources=data.resources
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                             Function Definitions                             #
# ---------------------------------------------------------------------------- #
# ----------------- Check resources if it is available or not ---------------- #
def check_resources(id):
    water_bool=True
    milk_bool=True
    coffee_bool=True
    water=menu[id]['ingredients']['water']
    milk=menu[id]['ingredients']['milk']
    coffee=menu[id]['ingredients']['coffee']
    water_resources=resources['water']
    milk_resources=resources['milk']
    coffee_resources=resources["coffee"]
    if water_resources<water:
        print("Sorry there is not enough water")
        water_bool=False
    if milk_resources<milk:
        print("Sorry there is not enough milk")
        milk_bool=False
    if coffee_resources<coffee:
        print("Sorry there is not enough coffee")
        coffee_bool=False
    if(water_bool==True and milk_bool==True and coffee_bool==True):
        return True
    else:
        return False
# ---------------------------------------------------------------------------- #
# ----------------------- check money with drink price ----------------------- #
def check_money(id,quarters,dimes,nickles,pennies):
    drink_cost=menu[id]['cost']
    payment=(quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
    if drink_cost>payment:
        change=-1
    else:
        change=payment-drink_cost
    return change
# ---------------------------------------------------------------------------- #
# ---------------- change resources due to consume the drinks ---------------- #
def change_resources(id):
    water=menu[id]['ingredients']['water']
    milk=menu[id]['ingredients']['milk']
    coffee=menu[id]['ingredients']['coffee']
    rest_of_water=resources['water']-water
    rest_of_milk=resources['milk']-milk
    rest_of_coffee=resources['coffee']-coffee
    new_resources={
        "water":rest_of_water,
        "milk":rest_of_milk,
        "coffee":rest_of_coffee,
    }
    return new_resources
# ---------------------------------------------------------------------------- #

user_choice=input("what would you like? (espresso/latte/cappuccino): ")
if user_choice=="espresso":
    print("please insert coins.")
    quarters=int(input("How many quarters? "))
    dimes=int(input("How many dimes? "))
    nickles=int(input("How many nickles? "))
    pennies=int(input("How many pennies? "))
    check_empty=check_resources("espresso")
    if check_empty==True:
        change=check_money("espresso")
        if change<0:
            print("sorry there is not enough money, money refunded !")
        else:
            print(f"Here is {change} in change")
            resources=change_resources("espresso")
            print("Here is your 'espresso' Enjoy !")

