from data import menu
from data import resources
from drink_modeling import DrinkModel
from coffee_machine_work import CoffeeMachine
from resources_modeling import MainResources
from finance import Finance
actual_resources=resources
profit=0
while True:
    user_choice=input("what would you like? (espresso/latte/cappuccino)? ")
    if user_choice=="report":
        print(f"Water: {actual_resources['water']}\nMilk:{actual_resources['milk']}\nCoffee:{actual_resources['coffee']}\nProfit:{profit}")
    elif user_choice=="off":
        break
    else:
        drink=DrinkModel(menu,user_choice)
        main_resources=MainResources(actual_resources)
        cofee_machine=CoffeeMachine(drink,main_resources)
        check_resources=cofee_machine.check_resources()
        if check_resources:
            print("please insert coins..")
            quarters=int(input("How many Quarters?  "))
            dimes=int(input("How many Dimes? "))
            nickles=int(input("How many Nickles? "))
            pennies=int(input("How many Pennies? "))
            finane=Finance(drink,quarters,dimes,nickles,pennies)
            check_payment=finane.check_payment()
            if check_payment:
                change=finane.return_change()
                print(f"here is {change} in change")
                print(f"here is your {user_choice} Enjoy ! ")
                actual_resources=main_resources.change_resources(drink)
                profit+=drink.cost
            else:
                print("sorry insufficient coins")
                break
        else:
            print("sorry insufficient resources")
            break
