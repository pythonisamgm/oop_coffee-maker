from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


espresso = MenuItem ("espresso", "50", "0", "18", "1.5")
cappuccino = MenuItem("cappuccino", "250", "150", "24", "3.0")
latte = MenuItem("latte", "200", "150", "24", "2.5")



is_on = True

while is_on:

    menu = Menu()
    drink_list = menu.get_items()
    choice = input(f"What would you like? {drink_list}: ")

    coffeemaker = CoffeeMaker()
    money_machine = MoneyMachine()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemaker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        enough_resources = coffeemaker.is_resource_sufficient(drink)
        if enough_resources:

            pago = money_machine.make_payment(drink.cost)
            if pago:
                hacer_cafe = coffeemaker.make_coffee(drink)










