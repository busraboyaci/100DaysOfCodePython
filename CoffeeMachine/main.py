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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def calculate(quarter, dime, nickle, pennie):
    return (quarter * 0.25) + (nickle * 0.05) + (dime * 0.10) + (pennie * 0.01)


def control_resource(user_resources, machine_resource):
    for key in user_resources:
        if user_resources[key] > machine_resource[key]:
            print(f"Sorry there is not enough {key}.")
            return False
        return True


def resource_subtract(machine_resource, user_resource):
    left_resources = {}
    for key in machine_resource:
        if key in user_resource:
            left_value = machine_resource[key] - user_resource[key]
            left_resources[key] = left_value
    return left_resources




def coffee_coast(user_input):
    cost = MENU[user_input]["cost"]
    coffee_cost = round((calculated_money - cost), 2)
    if cost <= calculated_money:
        print(f"Here is ${coffee_cost} in change.")
        return coffee_cost
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

should_continue = True
while should_continue:

    users_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if users_input == "off":
        should_continue = False
    elif users_input == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Milk: {resources['milk']} ml")
    else:
        if control_resource(MENU[users_input]["ingredients"], resources):
            print("Please insert coins.")
            quarters = float(input("how many quarters?: "))
            dimes = float(input("how many dimes?: "))
            nickles = float(input("how many nickles?: "))
            pennies = float(input("how many pennies?: "))
            calculated_money = calculate(quarters, dimes, nickles, pennies)
            calculated_money = calculate(quarters, dimes, nickles, pennies)
            coffee_coast(users_input)
            make_coffee(users_input, MENU[users_input]["ingredients"])

