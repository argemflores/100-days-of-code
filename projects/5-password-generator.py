#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator! 🔑")
nr_letters= int(input(f"How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
is_random = input(f"Would you like it to be randomized (Y/N)?\n")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

# add random letters to password list
for _ in range(1, nr_letters + 1):
    password.append(random.choice(letters))

# add random symbols to password list
for _ in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

# add random numbers to password list
for _ in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

# shuffle password list if randomized
if is_random.upper() == 'Y':
    random.shuffle(password)

# print password
print('Your password:', ''.join(password))
