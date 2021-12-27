# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# compute days remaining
years_left = 90 - int(age)

# compute for years, weeks, and months
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

# print results using f-string
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
