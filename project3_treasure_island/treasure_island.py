print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("\nYou have gotten a hint on the location of the treasure and a key. You are walking on a road going towards the location you were given.")
crossroad_decision = input('You arrive at a crossroad and need to choose your direction. Do you go "left" or "right"? \nType your answer: ')

if crossroad_decision.lower() != "left":
    if crossroad_decision.lower() == "right":
        print("\nAs you stroll along the road on the right, the ground under you suddenly crumbles and you fall into a hole. \nGame Over!")
    else:
        print('\nStanding still unable to make a choice between "left" and "right", the ground under you weakens and suddenly crumbles and you fall into a hole. \nGame Over!')
else:
    print("\nYou choose the road on the left and start walking forward feeling good about your choice.")
    river_decision = input('Having walked for a while, you encounter a river blocking your path forward. Do you "swim or "wait? \nType your answer: ')

    if river_decision.lower() != "wait":
        if river_decision.lower() == "swim":
            print("\nAs you swim closer and closer to the river bank on the other side, a massive trout lunges at you. \nGame Over!")
        else:
            print('\nTrying to be clever, you try to find another way instead of just choosing to "swim" or "wait". Pacing back and forth thinking, you trip on a root and fall into the river. Noticing the disturbance, a massive trout lunges at you. \nGame Over!')
    else:
        print("\nAs you patiently wait, you see something moving along the river. It's a big log floating and moving towards you. The log hits some rocks, turns sideways and gets lodged against the rocks. You are able to walk along the log and hop to the other side.")
        door_decision = input('Continuing from the river you see an old building. You inspect it all around and find three doors you could enter through, one is "red", another "blue" and the third one "yellow". Which one fo you choose? \nType your answer: ')

        if door_decision.lower() != "yellow":
            if door_decision.lower() == "red":
                print("\nYou turn the nob of the red door and start to open it... You hear a suspicious click sound and before you can back away, you are engulfed in flames by a vicious trap. \nGame Over!")
            elif door_decision.lower() == "blue":
                print("\nYou turn the nob of the blue door and open it. Everything seems safe so you move inside. As you reach the middle of this grand dark room, series of cage doors fly open and multiple beasts surround you. There's nothing you can do against them. \nGame Over!")
            else:
                print('\nScared by the this old building, you choose not to enter neither of the "red", "blue" or "yellow" doors. Yoy walk away empty handed with no treasure. \nGame Over!')
        else:
            print("\nYou turn the nob of the yellow door and open it. You see stairs leading underground into a cellar. As you enter and your eyes adjust, you start seeing old peculiar objects dusty and filled with cobwebs. In the middle there's a chest. You try the key and it fits. As the glimmer of the treasure hits your face, you know you have won. \nCongratulations!")