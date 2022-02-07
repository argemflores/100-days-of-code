#Write your code below this line 👇

# check if a number is prime or not
def prime_checker(number):
    # set flags
    not_prime = False
    x = number - 1

    # divide the number by the number - 1
    while x > 1 and not not_prime:
        # number is divisible by x (exit loop)
        if number % x == 0:
            not_prime = True

        # check the next number - 1
        x -= 1

    # print results
    if not_prime:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
