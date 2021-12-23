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
    for key in machine_resource:
        if key in user_resources and user_resources[key] <= machine_resource[key]:
            return True
        else:
            return False


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
    return coffee_cost


def make_coffee():
    print(f"Here is ${coffee_coast(users_input)} in change.")
    print(f"Here is your {users_input} ☕️. Enjoy!")


# TODO: How to get the user drink ingredient and computers written

resource_control = True
should_continue = True
while should_continue:

    users_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    user_resource = MENU[users_input]["ingredients"]
    resource_control = control_resource(user_resource, resources)

    if resource_control:
        print("Please insert coins.")
        quarters = float(input("how many quarters?: "))
        dimes = float(input("how many dimes?: "))
        nickles = float(input("how many nickles?: "))
        pennies = float(input("how many pennies?: "))
    elif not resource_control:
        for key in resources:
            if resources[key] < user_resource[key]:
                should_continue = False
        print(f"Sorry there is not enough {key}.")

    calculated_money = calculate(quarters, dimes, nickles, pennies)
    # TODO: 1.a. Check the user’s input to decide what to do next.
    if resource_control:
        coffee_coast(users_input)
        make_coffee()

    resources = resource_subtract(resources, user_resource)