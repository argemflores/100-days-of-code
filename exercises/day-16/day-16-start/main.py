import another_module
# print(another_module.another_variable)

# import
from turtle import Turtle, Screen

# create turtle
timmy = Turtle()
print(timmy)

# change shape and color
timmy.shape("turtle")
timmy.color("white")

# move 100 paces
timmy.forward(100)

# create screen
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
