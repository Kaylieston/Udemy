number = int(input("Please input a number: "))

if number % 2 == 0: 
    print("This number is even.")
else: 
    print("This number is odd.")


height = int(input("Please input your height: "))
bill = 0
if height > 120:
    print("You can go on a ride!")
# Age for ticket price
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Your ticket price is $5")
    elif age <= 18:
        bill = 7
        print("Your ticket price is $7")
    elif age > 18:
        bill = 12
        print("Your ticket price is $12")
# If customers want to take photo
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No." )
    if wants_photo == "y":
        bill += 3 

    print(f"Your final bill is {bill}. ")


else:
    print("You can't ride this rollercoaster")

""""""""""""""""""""""""""""""""""""
weight = 85
height = 1.85

bmi = weight / (height ** 2)
print(bmi)
# 🚨 Do not modify the values above
# Write your code below 👇


if bmi >= 25:
    print("overweight")
elif bmi < 18.5: 
    print("underweight")

else: 
    print("normal weight")

""""""""""""""""""""""""""""""""""""""
# PIZZA DELIVERY BILL 
print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0 

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
if size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
if size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
else:
    print("You've input wrong format to order")
print(f"Your final bill is: ${bill}.")

""""""""""""""""""""""""""""""""""""""""""
# #Another way to do this feature 

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0 

# Todo: work out how much they need to pay based on their size choice. 
if size == "S":
    bill += 15
elif size == "M":
    bill += 20 
elif size == "L":
    bill += 25
else: 
    print("You typed the wrong inputs!")
    
# Todo: work out how much to add to their bill based on the pepperoni choice. 
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3 

# Todo: work out their final amount based on extra cheese choosen. 
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# TREASURE GAME 

def main():

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
    /______/______/______/______/______/______/______/______/______/______/[TomekK]
    ******************************************************************************
    ''')

    print("Welcome to Treasure Island.\nYour mission is to find the treasure ^^.")

    # Cross Road 
    print("You're at a cross road. Where do you want to go?\n")

    keyword_cross_road = input("   Type \"left\" or \"right\": ").lower() #lower() to accept multiple case sensitive
    if keyword_cross_road == "left":
        print("You've come to a lake. There is an island in the middle of the lake.")
    elif keyword_cross_road == "right":
        print("You fell into a hole and lost to Wonderland.")
    else: 
        print("Game Over. T.T")
        return
    # lake 
    keyword_lake = input("   Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ").lower()
    if keyword_lake == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. ")
    else: 
        print("You're attacked by trout. GAME OVER!!!!")
        return
    # Door 
    keyword_door = input("One red, one yellow and one blue. Which color do you choose? ").lower()
    if keyword_door == "red":
        print("Burned by fire. GAME OVER!!")
        return
    elif keyword_door == "yellow":
        print("You WIN !! ~~")
    elif keyword_door == "blue":
        print("Eaten by beasts. GAME OVER!!")
        return
    else: 
        print("Game over T.T")
        return
main()
