#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("💳 Welcome to the Tip Calculator!")

# get inputs from user
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# compute share per person (rounded off to 2 decimal places)
payment_per_person = round(bill * (1 + (0.01 * tip_percentage)) / people, 2)

# print results (formatted to 2 decimal places)
print(f"💵 Each person should pay: ${payment_per_person:.2f}")
