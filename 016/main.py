from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    
    choice = input(f"What would you like? {Menu.get_items()} : ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "off":
        print("Going off ......")
        is_on = False

    elif Menu.find_drink(choice) and coffee_maker.is_resource_sufficient(Menu.find_drink(choice)) and money_machine.make_payment(Menu.find_drink(choice).cost):
        coffee_maker.make_coffee(Menu.find_drink(choice))
