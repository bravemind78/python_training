import data
# ---------------------------------------------------------------------------- #
#                             Variables Defintions                             #
# ---------------------------------------------------------------------------- #
# ---------------------------- modules Defintions ---------------------------- #
menu=data.menu
resources=data.resources
sales=[]
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
# ------- Give a complete report for resources of wate,milk and coffee ------- #
def report(resources,sales):
    water=resources['water']
    milk=resources["milk"]
    coffee=resources['coffee']
    money=sum(sales)
    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}")
    # ---------------------------------------------------------------------------- #
    # ----------------------- choose the drink and make it ----------------------- #
def chosen_drink(id,resources):
    print("please insert coins.")
    quarters=int(input("How many quarters? "))
    dimes=int(input("How many dimes? "))
    nickles=int(input("How many nickles? "))
    pennies=int(input("How many pennies? "))
    check_empty=check_resources(id)
    if check_empty==True:
        change=check_money(id,quarters,dimes,nickles,pennies)
        if change<0:
            print("sorry there is not enough money, money refunded !")
        else:
            print(f"Here is {change} in change")
            resources=change_resources(id)
            print(f"Here is your {id} Enjoy !")
            sales.append(menu[id]['cost'])
    return resources
# ---------------------------------------------------------------------------- #
# ----------------------- FullFill all resources again ----------------------- #
def fullfill_resources():
    resources_original={
    "water": 300,
    "milk": 200,
    "coffee": 100}
    print("the machine succeeded fullfill !")
    return resources_original
# ---------------------------------------------------------------------------- #
while True:
    user_choice=input("what would you like? (espresso/latte/cappuccino): ")
    if user_choice=="espresso":
       resources=chosen_drink("espresso",resources)
    elif user_choice=="latte":
       resources=chosen_drink("latte",resources)
    elif user_choice=="cappuccino":
        resources=chosen_drink("cappuccino",resources)
    elif user_choice=="report":
        report(resources,sales)
    elif user_choice=="fullfill":
        resources=fullfill_resources()
    elif user_choice=="turn off":
        break
