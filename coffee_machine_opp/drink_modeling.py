class DrinkModel:
    def __init__(self,menu,d_name):
        self.drink_name=d_name
        self.water=menu[d_name]['ingredients']['water']
        self.milk=menu[d_name]['ingredients']['milk']
        self.coffee=menu[d_name]['ingredients']['coffee']
        self.cost=menu[d_name]['cost']
