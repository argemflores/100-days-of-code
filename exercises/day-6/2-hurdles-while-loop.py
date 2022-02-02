# Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# Hurdle's While Loop Challenge

# turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# jump one hurdle
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# navigate through the obstacles until goal is reached
while not at_goal():
    # jump if there is a hurdle
    if wall_in_front():
        jump()
    else:
        move()
