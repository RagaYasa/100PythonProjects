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
print("You've been got into the Treasure Island safely.\nNow is the time we find the treasure!!")

direction = input("Which way should we go? left or right?\n").lower()
right = "right".lower() #lower() to make any input or str go lowercase
left = "left".lower()

if direction == right :#or right == "RIGHT" :#
    print("You've find yourself to canibal village, and get stolen by the vilager\n!!Game Over!!")

elif direction == left :
    print("Congrats, you found a way to the jungle")
    cross_river = input("you've found away to the river. what you want a do?\nswim or wait?\n").lower()
    swim = "swim".lower()
    wait = "wait".lower()
    if cross_river == swim :
        print("You've been eaten by crocodile.\n!!Game Over!!")
    elif cross_river == wait :
        print("Congrats! youve find yourself a boat and get to the end of the river.")
        final_treasure = input("You've find yourself a great big door.\nThere is 3 of them, which door you want to go in?\nRed, Green or Blue?\n").lower()
        red = "red".lower()
        green = "green".lower()
        blue = "blue".lower()
        if final_treasure == red :
            print("Well, youve been fell into the lava pit\n!!GAME OVER!!")
        elif final_treasure == green :
            print("Whoops, You get hypnotized by the poison gas, and never come back.\n!!GAME OVER!!")
        elif final_treasure == blue :
            print("You found the treasure!! and you've teleported back to your ship.\n!!YOU WIN!!")

else:
    print("input a correct answer")