def turn_right():
    turn_left()
    turn_left()
    turn_left()

def orient_start():
    while not wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()

def to_goal():
    orient_start()
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()     
    
to_goal()