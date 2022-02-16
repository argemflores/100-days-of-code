# Simple Calculator 🧮
# https://replit.com/@ArgemFlores/calculator

import art

def add(n1, n2):
    """Add two numbers"""

    return n1 + n2

def subtract(n1, n2):
    """Subtract a number from another"""

    return n1 - n2

def multiply(n1, n2):
    """Multiple two numbers"""

    return n1 * n2

def divide(n1, n2):
    """Divide a number by another (except 0)"""

    if n2 > 0:
        return n1 / n2

    return 'Invalid'

def calculator():
    """Calculate two numbers using a chosen operation"""

    # initialize
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    choice = 'y'
    result = ''
    num1 = ''

    # ask for the 1st number
    num1 = input("What's the first number? ")

    # continue while choice is yes
    while choice == 'y':
        num1 = str(num1)

        # invalid number
        if not (num1.isnumeric() or num1.replace('.', '', 1).isdigit() or (num1.startswith('-') and num1[1:].isdigit())):
            print("Invalid number, try again")

            num1 = input("What's the first number? ")
        else:
            # print the operations
            for operation, function in operations.items():
                print(operation, '(' + function.__name__ + ')')

            # ask for the operation
            operator = input("Pick an operation: ")

            # valid operation
            if operator in operations.keys():
                num2 = input("What's the next number? ")

                if not (num2.isnumeric() or num2.replace('.', '', 1).isdigit() or (num2.startswith('-') and num2[1:].isdigit())):
                    print("Invalid number")
                else:
                    if '.' not in num1 or num1[-2:] == '.0':
                        # convert num1 to int if not float
                        num1 = int(num1)
                    else:
                        num1 = float(num1)

                    if '.' not in num2 or num2[-2:] == '.0':
                        # convert num2 to int if not float
                        num2 = int(num2)
                    else:
                        num2 = float(num2)

                    # compute based on chosen operation
                    result = operations[operator](num1, num2)

                    if result != 'Invalid':
                        if '.' not in str(result) or str(result)[-2:] == '.0':
                            # convert result to int if not float
                            result = int(result)

                        # print results
                        print(f"Answer: {num1} {operator} {num2} = {result}")

                        # store the result to number 1 if valid
                        num1 = result
                    else:
                        print(f"Invalid, result {num1} remains")

                    # ask to continue calculating or to exit loop
                    choice = input(f"Type 'y' to continue calculating with {num1}, 'n' to start a new calculation, 'x' to exit: ").lower()

                    if choice == 'n':
                        # start a new calculation
                        calculator()
            else:
                # invalid operation
                print("Invalid operation, try again")

print(art.logo)

# start calculator
calculator()

print("Thanks for using Simple Calculator! 🧮")
