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
print("Welcome to Treasure Island. 🏝")
print("Your mission is to find the treasure. ⭐️")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input('🛣 A fork in the road! Where do you want to go: left or right? ').lower()

if direction == 'left':
    action = input('🌊 You saw a vast ocean! What do you want to do: swim or wait? ').lower()

    if action == 'wait':
        door = input('🚪 Three magical doors appear! You enter: red, blue or yellow? ').lower()

        if door == 'red':
            print('Waaah! You are being burned alive! Game over! 🔥')
        elif door == 'blue':
            print('Noooo! Blue-scaled beasts attack you! Game over! 🦕')
        elif door == 'yellow':
            print('Yeeey! You found the treasure! Congratulations! 👑')
        else:
            print('Awwww! You are out of luck! Game over! ❌')
    else:
        print('Oh no! A monster shark devours you alive! Game over! 🦈')
else:
    print('Ooops! You fell into a trap full of spikes! Game over! 🕳')
