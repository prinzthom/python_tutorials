MENU_ITEMS= {
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

income = 0
resources = {
    "water": 300,
    "milk": 300,
    "coffee": 300,
}
history = dict(
        espresso=0,
        latte=0,
        cappuccino=0
)
menu=["espresso","latte","cappuccino"]
options=["order","report","end"]


def item_order_possible(item_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in item_ingredients:
        if item_ingredients[item] > resources[item]:
            print(f"​Sorry we do not have enough anymore {item}.")
            return "can not"
    return "can"


def payment_collection():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total = quarters+dimes+nickles+pennies
    return total


def payment_validation(money_received, item_cost):
    if money_received >= item_cost:
        change = round(money_received - item_cost, 2)
        print(f"Here is you'r change :${change}.")
        global income
        income += item_cost
        return "enough"
    else:
        print("Sorry that's not enough money.")
        print("You have been refunded.")
        return "not enough"


def prepare_order(item_name, item_ingredients):
    for item in item_ingredients:
        resources[item] = resources[item] - item_ingredients[item]
    history[item_name]=history[item_name]+1
    print(f"enjoy you'r {item_name}")


idle = False

while not idle:
    option = input(f"​What would you like to do? {options}: ")

    if option=="order":
        item_option = input(f"​What would you like order? {menu}: ")
        item = MENU_ITEMS[item_option]
        if item_order_possible(item["ingredients"])=="can":
            payment = payment_collection()
            if payment_validation(payment, item["cost"])=="enough":
                prepare_order(item_option, item["ingredients"])
    
    elif option == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"total income: ${income}")
        print(f"order history:{history}")

    elif option == "end":
        idle = True
    
    else:
        idle=True