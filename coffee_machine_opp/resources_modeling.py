class MainResources:
    def __init__(self,resources):
        self.water=resources['water']
        self.milk=resources['milk']
        self.coffee=resources['coffee']
# ---------------------------------------------------------------------------- #
#                              Methods Definitions                             #
# ---------------------------------------------------------------------------- #
# ----------------------------- change resources ----------------------------- #
    def change_resources(self,drink):
        water=self.water-drink.water
        milk=self.milk-drink.milk
        coffee=self.coffee-drink.coffee
        new_resources={"water": water,"milk":  milk,"coffee": coffee,}
        return new_resources
# ---------------------------------------------------------------------------- #