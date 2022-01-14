# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# normalize combined names
names = (name1 + ' ' + name2).lower()
true_count = 0
love_count = 0

# count TRUE occurrences
true_count += names.count('t')
true_count += names.count('r')
true_count += names.count('u')
true_count += names.count('e')

# count LOVE occurrences
love_count += names.count('l')
love_count += names.count('o')
love_count += names.count('v')
love_count += names.count('e')

# format true love score
true_love = int(str(true_count) + str(love_count))

# interpret true love score
if true_love < 10 or true_love > 90:
    print(f'Your score is {true_love}, you go together like coke and mentos.')
elif 40 <= true_love <= 50:
    print(f'Your score is {true_love}, you are alright together.')
else:
    print(f'Your score is {true_love}.')
