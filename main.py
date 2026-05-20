from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffeeMachine = "on"
coffee = Menu()
reports = CoffeeMaker()


while coffeeMachine == "on":

    choice = input(f"What would you like? {coffee.get_items()}: ").lower()

    if choice == "off":
        coffeeMachine = "off"
    if choice == "report":
        print(reports.report())