class CoffeeMachine:
    def __init__(self,drink,main_resources):
        self.chosen_drink = drink
        self.main_resources = main_resources
# ---------------------------------------------------------------------------- #
#                              Methods Definitions                             #
# ---------------------------------------------------------------------------- #
# ---------------- Check resources if it is avaialable or not ---------------- #
    def check_resources(self):
        if self.chosen_drink.water<=self.main_resources.water and self.chosen_drink.milk<=self.main_resources.milk and self.chosen_drink.coffee<=self.main_resources.coffee:
            return True
        else:
            return False
# ---------------------------------------------------------------------------- #