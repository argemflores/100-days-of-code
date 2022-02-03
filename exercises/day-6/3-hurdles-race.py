# Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# Hurdle's Race

# turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# jump one hurdle
def jump():
    turn_left()

    # move up
    while wall_on_right():
        move()

    # change direction
    turn_right()
    move()
    turn_right()

    # move down
    while front_is_clear():
        move()

    turn_left()

# navigate through the obstacles until goal is reached
while not at_goal():
    # jump if there is a hurdle
    if wall_in_front():
        jump()
    else:
        move()
