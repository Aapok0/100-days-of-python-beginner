def move_until_wall():
    while front_is_clear():
        move()

def move_until_right():
    while wall_on_right():
        move()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move_until_wall()
    turn_left()
    move_until_right()
    turn_right()
    move()
    turn_right()
    move_until_wall()
    turn_left()
        
def to_goal():
    while not at_goal():
        jump()
            
to_goal()  