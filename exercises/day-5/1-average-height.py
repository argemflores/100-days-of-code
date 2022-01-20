# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
total_number = 0

# get total heights and total number of students
for height in student_heights:
    total_height += height
    total_number += 1

# compute for average then round it off
average_height = round(total_height / total_number)

print(average_height)
