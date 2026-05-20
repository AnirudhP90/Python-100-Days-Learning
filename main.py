from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink = (menu.find_drink(choice))
        if coffee_maker.is_resource_sufficient(drink):
            print(money_machine.make_payment(drink.cost))




