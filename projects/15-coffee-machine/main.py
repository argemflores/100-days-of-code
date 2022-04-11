import data


def ask_customer():
    """Prompt user by asking "What would you like? (espresso/latte/cappuccino): "."""

    # ask user, then remove spaces and set to lowercase
    choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

    # check if choice is valid
    if choice not in data.MENU.keys() and choice not in ['off', 'report']:
        # return False if invalid
        return False

    # valid choice
    return choice


def turn_off():
    """Turn off the Coffee Machine by entering "off" to the prompt."""

    # show turned off message
    print("Coffee machine is turned off. Thank you!")

    return False


def print_report(money):
    """Print report."""

    for resource, amount in data.resources.items():
        print(f"{resource.capitalize()}: {amount}ml")

    print(f"Money: ${money:.2f}")


def is_sufficient(coffee):
    """Check resources sufficient?"""

    # prepare resource list
    needed_resources = {}

    # check if resources have sufficient amount for the ingredient needed
    for ingredient, amount in data.MENU[coffee]['ingredients'].items():
        # ingredient does not have sufficient resource
        if data.resources[ingredient] < amount:
            # add to list of needed resources and the amount needed
            needed_resources[ingredient] = (data.resources[ingredient] - amount) * -1

    # all resources are sufficient
    if needed_resources == {}:
        return True

    # show insufficient resources
    print("Sorry, there is not enough: ")
    for resource, amount_needed in needed_resources.items():
        print(f"- {resource} ({amount_needed}ml needed)")

    return False

# TODO: 5. Process coins.

# TODO: 6. Check transaction successful?

# TODO: 7. Make coffee.


def main():
    money = 0.0
    is_running = True

    # ask customer
    choice = ask_customer()

    # process valid choice
    if choice is not False:
        if choice == 'off':
            # turn off coffee machine
            is_running = turn_off()
        elif choice == 'report':
            # print resources
            print_report(money)
        else:
            # check resources
            is_sufficient(choice)


if __name__ == '__main__':
    main()
