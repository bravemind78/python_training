class Finance:
    def __init__(self, drink,quarters,dimes,nickles,pennies):
        self.drink_cost=drink.cost
        self.quarters=quarters
        self.dimes=dimes
        self.nickles=nickles
        self.pennies=pennies
# ---------------------------------------------------------------------------- #
#                              MethodS Definitions                             #
# ---------------------------------------------------------------------------- #
# ------------- check payement if it is sufficient to pay or not ------------- #
    def check_payment(self):
        self.payment=(self.quarters*0.25)+(self.dimes*0.1)+(self.nickles*0.05)+(self.pennies*0.01)
        if self.payment>=self.drink_cost:
            return True
        else:
            return False
# ---------------------------------------------------------------------------- #
# ---------------------- calculate the a mount of change --------------------- #
    def return_change(self):
        change=self.payment-self.drink_cost
        return change
# ---------------------------------------------------------------------------- #