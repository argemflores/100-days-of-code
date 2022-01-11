# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Body Mass Index (BMI) = weight (kg) / height (m) squared
bmi = round(weight / height ** 2)

# print BMI results
print(f"Your BMI is {bmi}.")

# print BMI interpretation
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have normal weight.")
elif bmi < 30:
    print("You are overweight.")
elif bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")
