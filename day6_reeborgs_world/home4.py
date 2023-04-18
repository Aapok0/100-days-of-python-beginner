def move_until():
    while front_is_clear():
        move()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
def to_home():
    while not at_goal():
        if wall_in_front():
            if wall_on_right():
                turn_left()
            else:
                turn_right()
        elif front_is_clear:
            move_until()
            
to_home()