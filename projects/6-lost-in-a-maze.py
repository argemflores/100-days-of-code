# Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world.json&url=user_world%3Aproblem_world.json

# Lost in a Maze

# turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# find a right wall
while front_is_clear():
    move()
turn_left()

# navigate through the maze until goal is reached
while not at_goal():
    # turn left if stuck (wall in front and right)
    if wall_in_front() and not right_is_clear():
        turn_left()

    # move right if clear
    if right_is_clear():
        turn_right()

    # move forward if front is clear
    if front_is_clear():
        move()
