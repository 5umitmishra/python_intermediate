MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def item_ingredent(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry, there is not enough {item}")
            return False

    return True

def total_amount():
    """the total amount of coin incerted by the costumer"""
    print("please insert the coin")
    total = int(input("how many quaters ")) * 0.25
    total += int(input("how many Dime")) * 0.1
    total += int(input("how many Nickle")) * 0.05
    total += int(input("how many penny")) * 0.01
    return total

def is_money_recived(money_recived, drink_coat):
    if money_recived >= drink_coat:
        change = round(money_recived - drink_coat, 2)
        print(f"here's your change ${change}")
        global profit
        profit += drink_coat
        return True
    else:
        print("sorry not enough money")
        return False


def make_coffee(drink_name, order_ingredients):
    """ deduct the ingredient form the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here's is your {drink_name}☕. enjoy")


is_on = True

while is_on:
    choice = input("what would you like? (espresso / latte / cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk:  {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money ${profit}")

    else:
        drink = MENU[choice]
        if item_ingredent(drink["ingredients"]):
            payment = total_amount()
            if is_money_recived(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])


