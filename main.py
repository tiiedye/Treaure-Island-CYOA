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
print("Your mission is to find the treasure.\n")

print("You have just left the local village. After travelling a good amount you come to a fork in the road.")
l_or_r = input("Do you go left or right? (L or R): ")
l_or_r = l_or_r.lower()

if l_or_r == "l":
    print("You cautiously chose the left path and soon come across a body of water...")
    s_or_w = input("Do you swim or wait? (S or W): ")
    s_or_w = s_or_w.lower()
    if s_or_w == "w":
        print("You wait a while, and just as you think of turning to go home a fisherman on his small boat sails into "
              "view. You waive him down and he offers to give you a lif across the lake.")
        print("After crossing the lake and travelling a bit longer you come across a building with 3 doors, "
              "a red door, a yellow door, and a blue door.")
        r_y_b = input("Which door do you chose? (R, Y, or B): ")
        r_y_b = r_y_b.lower()

        if r_y_b == "y":
            print("You open the door to find the room filled to the brim with any treasure you can imagine! "
                  "Congratulations! You won!")
        elif r_y_b == "r":
            print("You enter the room and see nothing, but the door closes behind you. Soon the room is filled with "
                  "flames and you burn to death.")
            print("Game Over!")
        elif r_y_b == "b":
            print("You enter the room, and the door slams shut behind you. You hear a rustling as the noise seems to "
                  "have awakened something. You are attacked and devoured by many beasts.")
            print("Game Over!")
        else:
            print("You decided to open none of the doors. You returned home empty handed...")
            print("Game Over!")
    elif s_or_w == "s":
        print("You begin swimming. You're halfway across the lake, but then you feel something nibble at your leg. "
              "Moments later you are swallowed whole by a giant trout. You died!")
        print("Game Over!")
    else:
        print("You decided neither to swim or wait. You returned home empty handed...")
        print("Game Over!")
elif l_or_r == "r":
    print("You march along the right path confidently, nose pointed high. Perhaps too confidently, as ypu do not "
          "notice the pitfall trap before you. You fall into the hole and die.")
    print("Game Over!")
else:
    print("You decided neither left or right. You sit at the crossroads wrecked with indecision. Time passes. Soon "
          "you are out of rations and water. You die of thirst before you can die of hunger...")
    print("Game Over!")

