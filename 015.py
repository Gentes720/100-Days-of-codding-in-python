import sys
import math
menu = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
    "cost": 1.50
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
    "cost": 2.50
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
    "cost": 3.00
    }
}

ressources = {
    "water":600,
    "coffee": 200,
    "milk": 300,
    "money": 0
}

def report():
    print(f'water : {ressources["water"]} mL')
    print(f'coffee : {ressources["coffee"]}g')
    print(f'milk: {ressources["milk"]}mL')
    print(f'money : ${ressources["money"]}')
    new_cup()

def check_espresso():
    if ressources["water"] < 50:
        print("Sorry there is not enough water")
        new_cup()
    elif ressources["coffee"] < 18:
        print("Sorry there is not enough cofee")
        new_cup()
def check_latte():
    if ressources["water"] < 200:
        print("Sorry there is not enough water")
        new_cup()
    elif ressources["coffee"] < 24:
        print("Sorry there is not enough cofee")
        new_cup()
    elif ressources["milk"] < 150:
        print("Sorry there is not enough milk")
        new_cup()
    
def check_cappuccino():
    if ressources["water"] < 250:
        print("Sorry there is not enough water")
        new_cup()
    elif ressources["coffee"] < 24:
        print("Sorry there is not enough cofee")
        new_cup()
    elif ressources["milk"] < 100:
        print("Sorry there is not enough milk")
        new_cup()
def process_money():
    money = 0.00
    quaters = int(input(" How many quaters :"))
    dimes =   int(input(" How many dimes :"))
    nickels = int(input(" How many nickels :"))
    pennies = int(input(" How many pennies :"))

    money = 0.25 * quaters + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if choice == "espresso" and money >= menu['espresso']['cost']:
        print(f"Here is ${round((money - menu['espresso']['cost']),3)} in change")
        ressources["money"] += menu['espresso']['cost']
    elif choice == "latte" and money >= menu['latte']['cost']:
        print(f"Here is ${round((money - menu['latte']['cost']),3)} in change")
        ressources["money"] += menu['latte']['cost']
    elif choice == "cappuccino" and money >= menu['cappuccino']['cost']:
        print(f"Here is ${round((money - menu['cappuccino']['cost']),3)} in change")
        ressources["money"] += menu['cappuccino']['cost']
    else:
        print("Sorry that's not enough money. Money refunded!")
        new_cup()

def make_coffee(ressources, menu):
    if choice == "espresso":
        ressources["water"]-= menu["espresso"]["ingredients"]["water"]
        ressources["coffee"]-= menu['espresso']["ingredients"]['coffee']
        ressources["milk"]-= menu['espresso']["ingredients"]['milk']
        print("Here us your espresso!! Enjoy")
        new_cup()
    elif choice == "latte":
        ressources["water"]-= menu['latte']["ingredients"]['water']
        ressources["coffee"]-= menu['latte']["ingredients"]['coffee']
        ressources["milk"]-= menu['latte']["ingredients"]['milk']
        print("Here us your latte!! Enjoy")
        new_cup()
    elif choice == "cappuccino":
        ressources["water"]-= menu['cappuccino']["ingredients"]['water']
        ressources["coffee"]-= menu['cappuccino']["ingredients"]['coffee']
        ressources["milk"]-= menu['cappuccino']["ingredients"]['milk']
        print("Here us your cappuccino!! Enjoy")
        new_cup()

def new_cup():
    global choice
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        report()
    elif choice == "espresso":
        check_espresso()
    elif choice == "latte":
        check_latte()
    elif choice == "cappuccino":
        check_cappuccino()
    elif choice == "off":
        sys.exit()
    else:
        print("invalid choice")
        new_cup()
    process_money()
    make_coffee(ressources, menu)

new_cup()