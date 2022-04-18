import data


def ask_customer():
    """Prompt user by asking "What would you like? (espresso/latte/cappuccino): "."""

    # print menu of coffee
    print_menu()

    # ask user, then remove spaces and set to lowercase
    choice = input("\n🤖 What would you like? (espresso/latte/cappuccino): ").strip().lower()

    # check if choice is valid
    if choice not in data.MENU.keys() and choice not in ['off', 'report']:
        # return False if invalid
        return False

    # valid choice
    return choice


def turn_off():
    """Turn off the Coffee Machine by entering "off" to the prompt."""

    print_report()

    # show turned off message
    print("🔘 Coffee machine is turned off. Thank you!")

    return False


def print_menu():
    """Print menu."""

    print("\n☕️ Menu")

    # print every coffee in the menu and their amount
    for coffee, info in data.MENU.items():
        if coffee != 'money':
            print(f"* {coffee.capitalize()}: ${info['cost']:.2f}")


def print_report():
    """Print report."""

    print("\n🧾 Report")

    # print every resource and their amount
    for resource, amount in data.resources.items():
        print(f"* {resource.capitalize()}: {amount}ml")

    # print current money
    print(f"* Money: ${data.MENU['money']:.2f}")


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
    print("❌ Sorry, there is not enough: ")
    for resource, amount_needed in needed_resources.items():
        print(f"   - {resource.capitalize()} ({amount_needed}ml more needed)")

    # not sufficient resources
    return False


def ask_coins(denomination):
    """Ask coins and validate payment"""

    # continue asking until correct number is provided
    while True:
        # ask for the number of coins
        coins = input(f"   How many {denomination}? ").strip()

        # payment is valid or empty (0)
        if not coins or coins.isnumeric():
            # convert empty to 0 coins
            if not coins:
                coins = 0
            break
        else:
            # payment is invalid, ask again
            print("❌ Invalid payment, please try again.")

    # return number of coins
    return int(coins)


def process_order(coffee):
    """Process payment and coffee."""

    # ask payment
    print("🪙 Please insert coins.")

    # ask number of coins for every denomination
    quarters = ask_coins("quarters")
    dimes = ask_coins("dimes")
    nickels = ask_coins("nickels")
    pennies = ask_coins("pennies")

    # compute payment
    payment = round(0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies, 2)

    # get current money and cost of coffee
    cost = data.MENU[coffee]['cost']
    money = data.MENU['money']

    # payment is not enough
    if payment < cost:
        # order is not successful
        print(f"❌ Sorry that's not enough money (needs ${cost:.2f}). Money refunded.")

        return False
    else:
        # payment is too much
        if payment > cost:
            # return change to customer
            change = round(payment - cost, 2)

            print(f"Here is ${change:.2f} in change.")

        # deduct resources
        for resource, amount in data.MENU[coffee]['ingredients'].items():
            data.resources[resource] -= amount

        # payment successful, add to money
        data.MENU['money'] = round(money + cost, 2)

    return True


def main():
    # set default money
    data.MENU['money'] = 0.0

    # continue asking until turned off
    while True:
        # ask customer
        choice = ask_customer()

        # process valid choice
        if choice is False:
            print("❌ Invalid choice, please try again.")
        else:
            if choice == 'off':
                # turn off coffee machine
                turn_off()
                break
            elif choice == 'report':
                # print resources
                print_report()
            else:
                # check resources
                if is_sufficient(choice):
                    # process payment and coffee
                    if process_order(choice):
                        # payment and coffee successful
                        print_report()
                        print(f"✅ Here is your {choice}. Enjoy! ☕️")


if __name__ == '__main__':
    main()
