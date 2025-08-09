print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

choice1 = input('Your\'re at a crossroad, where do you want to go? Tpye "Left" of "Right".').lower()

if choice1 == "left":

    #Continue the game
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" for a boat or just "Swim".').lower()
    if choice2 == "wait":

        #Continue the game
        choice3 = input('You\'ve came to a house with three doors. Pick one "Red", "Yellow", "Blue".').lower()
        if choice3 == "red":
            print("You got Sypfilis! - Game Over!")
        elif choice3 == "yellow":
            print("Congrats! You won all of the onions!")
        elif choice3 == "blue":
            print("It was all a dream! - Game Over!")
        else:
            print("You have to make a choice - Game Over!")
    else:
        print("You got attached by an angry Karen! Game Over!")

else:
    print("You fell in to a holde. Game Over!")
