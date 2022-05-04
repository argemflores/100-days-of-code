import another_module
print(another_module.another_variable)

# import classes
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

# import class
from prettytable import PrettyTable

table = PrettyTable()

# https://pokemondb.net/pokedex/all

# add columns and rows
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# change to left alignment
table.align = "l"

# print table
print(table)
