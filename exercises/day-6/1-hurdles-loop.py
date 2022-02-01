# Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Hurdle's Loop Challenge

# turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# jump one hurdle
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# jump 6 times
for j in range(1, 7):
    jump()
