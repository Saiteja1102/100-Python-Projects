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
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')

print("Welcome to Treasure Island..")
print("Your mission to find treasure")

l_r = input("You are approching a road, Do you want to go left or right? ")
l_r = l_r.lower()
if l_r == "right":
    print("There is no way to the right , Game Over")
else:
    sw_w = input("You are near to a river, Do u want to swim or wait? ")
    sw_w = sw_w.lower()
    if sw_w == "swim":
        print("You don't know swimming, Game Over")
    else:
        colour = input("There are three colour door U want which color Red , Yellow, Blue? ")
        colour = colour.lower()
        if colour == "red":
            print("You enterd a blood room, Game Over")
        elif colour == "blue":
            print("You entered a room filled with gosts, Game Over")
        else:
            print("You Win!!")


