#Write your code below this row 👇

# generate numbers from 1 to 100
for number in range(1, 101):
    message = ''

    # number is divisible by 3
    if number % 3 == 0:
        message = 'Fizz'

    # number is divisible by 5
    if number % 5 == 0:
        message += 'Buzz'

    # number is regular
    if message == '':
        message = number

    print(message)
