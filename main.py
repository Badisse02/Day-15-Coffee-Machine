def espresso(a):
    global resources
    resources["water"] -= 50
    resources["coffee"] -= 18
    resources['money'] += 1.5
    return a - 1.5


def latte(a):
    global resources
    resources["water"] -= 200
    resources["milk"] -= 150
    resources["coffee"] -= 24
    resources['money'] += 2.5
    return a - 2.5


def cappuccino(a):
    global resources
    resources["water"] -= 250
    resources["milk"] -= 100
    resources["coffee"] -= 24
    resources['money'] += 3.0
    return a-3.0


def report():
    global resources
    rep = f"water: {resources['water']}ml\nmilk: {resources['milk']}ml\ncoffee: {resources['coffee']}g"
    return rep+f"\nmoney: ${resources['money']}"


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
        "function": espresso,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
        "function": latte,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
        "function": cappuccino,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check(choice):
    a = MENU[choice]["ingredients"]
    if a["water"] <= resources["water"] and a["milk"] <= resources["milk"] and a["coffee"] <= resources["coffee"]:
        return True
    else:
        if a["water"] > resources["water"]:
            print("Sorry there is not enough water.")
        elif a["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough coffee.")
        return False


message = ""
messages = ["espresso", "latte", "cappuccino", "report", "off"]
while message not in messages:
    message = input("   What would you like? (espresso/latte/cappuccino): ")
while message in messages:
    if message != "off":
        if message != "report":
            if check(message):
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                money = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
                if money >= MENU[message]["cost"]:
                    money = MENU[message]["function"](money)
                    print(f"Here is ${'{:.2f}'.format(money)} in change.\nHere is your {message} ☕. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
        else:
            print(report())
        message = input("   What would you like? (espresso/latte/cappuccino): ")
        while message not in messages:
            message = input("   What would you like? (espresso/latte/cappuccino): ")
    else:
        print("Coffe machine turned off")
        break
