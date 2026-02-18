print("""Welcome to Treasure Island.
    Your mission is to find the treasure.
    You're at a cross road. Where do you want to go?
""")

input1 = input("Type 'left' or 'right' ").lower()
print(input1)

if input1 == "right":
    print("Game Over.")
elif input1 == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    input2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    print(input2)

    if input2 == "swim":
        print("Game Over.")
    elif input2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        input3 = input("Type 'red', 'yellow' or 'blue' ").lower()
        print(input3)
        if input3 == "red" or input3 == "blue":
            print("Game Over.")
        elif input3 == "yellow":
            print("You Win!")
    else: 
        # TODO: as for input and start the game
        print("Invalid input.")
else: 
    # TODO: as for input and start the game
    print("Invalid input.")



