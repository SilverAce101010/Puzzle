def Move_Room(celar_found, current_room):
    if celar_found == True:
        player_input = input("""Which room would you like to move to
        1. Grand Hall
        2. Study
        3. Library
        4. Dinning Room
        5. Kitchen
        6. Parlor
        7. Servants' Quarters
        8. Guest Bedrooms
        9. Garden & Greenhouse
        10. Main Bedroom
        11. Cellar
        : """)
    else:
        player_input = input("""Which room would you like to move to
        1. Grand Hall
        2. Study
        3. Library
        4. Dinning Room
        5. Kitchen
        6. Parlor
        7. Servants' Quarters
        8. Guest Bedrooms
        9. Garden & Greenhouse
        10. Main Bedroom
        : """)
    if player_input == "":
        print("You have not moved")
        player_input = current_room
    else:
        print("You have moved")
    return player_input

def Search_room(current_room):
    if current_room == "1": #Grand Hall
        player_input = input("""Where do you want to search
        1. 
        2. 
        3. 
        4. 
        5. 
        : """)
        if player_input == "1":
            print("")

        elif player_input == "2":
            print("")

        elif player_input == "3":
            print("")

        elif player_input == "4":
            print("")

        elif player_input == "5":
            print("")

        else:
            print("Invalid input")

    elif current_room == "2": #Study
        player_input = input("""Where do you want to search
        1. 
        2. 
        3. 
        4. 
        5. 
        : """)
        if player_input == "1":
            print("")

        elif player_input == "2":
            print("")

        elif player_input == "3":
            print("")

        elif player_input == "4":
            print("")

        elif player_input == "5":
            print("")

        else:
            print("Invalid input")

    elif current_room == "3": #Library
        player_input = input("""Where do you want to search
        1. The desk
        2. The carpet
        3. The bookshelf
        4. The chandelier
        5. The fireplace
        : """)
        if player_input == "1":
            print("You can see many important papers lying on and around the desk")

        elif player_input == "2":
            print("You notice that the carpet around the door way been torn slightly.")

        elif player_input == "3":
            print("As you pull a book from the shelf it opens a secret passage.")

        elif player_input == "4":
            print("You can tell that many of the candles on the chandalier have not been relit.")

        elif player_input == "5":
            print("You can tell that the fireplace was recently lit.")

        else:
            print("Invalid input")

    elif current_room == "4": #Dinning Room
        player_input = input("""Where do you want to search
        1. 
        2. 
        3. 
        4. 
        5. 
        : """)
        if player_input == "1":
            print("")

        elif player_input == "2":
            print("")

        elif player_input == "3":
            print("")

        elif player_input == "4":
            print("")

        elif player_input == "5":
            print("")

        else:
            print("Invalid input")

    elif current_room == "5": #Kitchen
        player_input = input("""Where do you want to search
        1. 
        2. 
        3. 
        4. 
        5. 
        : """)
        if player_input == "1":
            print("")

        elif player_input == "2":
            print("")

        elif player_input == "3":
            print("")

        elif player_input == "4":
            print("")

        elif player_input == "5":
            print("")

        else:
            print("Invalid input")

    elif current_room == "6": #Parlor
        player_input = input("""Where do you want to search
        1. 
        2. 
        3. 
        4. 
        5. 
        : """)
        if player_input == "1":
            print("")

        elif player_input == "2":
            print("")

        elif player_input == "3":
            print("")

        elif player_input == "4":
            print("")

        elif player_input == "5":
            print("")

        else:
            print("Invalid input")

    elif current_room == "7": #Servants' Quarters
        player_input = input("""Where do you want to search
        1. 
        2. 
        3. 
        4. 
        5. 
        : """)
        if player_input == "1":
            print("")

        elif player_input == "2":
            print("")

        elif player_input == "3":
            print("")

        elif player_input == "4":
            print("")

        elif player_input == "5":
            print("")

        else:
            print("Invalid input")

    elif current_room == "8": #Guest Bedrooms
        player_input = input("""Where do you want to search
        1. 
        2. 
        3. 
        4. 
        5. 
        : """)
        if player_input == "1":
            print("")

        elif player_input == "2":
            print("")

        elif player_input == "3":
            print("")

        elif player_input == "4":
            print("")

        elif player_input == "5":
            print("")

        else:
            print("Invalid input")

    elif current_room == "9": #Garden & Greenhouse
        player_input = input("""Where do you want to search
        1. 
        2. 
        3. 
        4. 
        5. 
        : """)
        if player_input == "1":
            print("")

        elif player_input == "2":
            print("")

        elif player_input == "3":
            print("")

        elif player_input == "4":
            print("")

        elif player_input == "5":
            print("")

        else:
            print("Invalid input")

    elif current_room == "10": #Main Bedroom
        player_input = input("""Where do you want to search
        1. 
        2. 
        3. 
        4. 
        5. 
        : """)
        if player_input == "1":
            print("")

        elif player_input == "2":
            print("")

        elif player_input == "3":
            print("")

        elif player_input == "4":
            print("")

        elif player_input == "5":
            print("")

        else:
            print("Invalid input")

    elif current_room == "11": #Cellar
        player_input = input("""Where do you want to search
        1. 
        2. 
        3. 
        4. 
        5. 
        : """)
        if player_input == "1":
            print("")

        elif player_input == "2":
            print("")

        elif player_input == "3":
            print("")

        elif player_input == "4":
            print("")

        elif player_input == "5":
            print("")

        else:
            print("Invalid input")

    else:
        print ("Invalid input")

def Question_suspect(current_room):
    if current_room == "1": #Grand Hall
        player_input = input("""Who would you like to question
        1. Dr. Victor Langley
        2. Margaret Holloway
        3. James Thornton
        4. Rebecca Clarke
        5. Mr. Edward Finch
        6. Arnold Gray
        : """)
        if player_input == "1":
            print("")
        elif player_input == "2":
            print("")
        elif player_input == "3":
            print("")
        elif player_input == "4":
            print("")
        elif player_input == "5":
            print("")
        elif player_input == "6":
            print("")
        else:
            print ("Invalid input")

    elif current_room == "2": #Study
        player_input = input("""Who would you like to question
        1. Dr. Victor Langley
        2. Margaret Holloway
        : """)
        if player_input == "1":
            print("")
        elif player_input == "2":
            print("")
        else:
            print ("Invalid input")

    elif current_room == "3": #Library
        player_input = input("""Who would you like to question
        1. Rebecca Clarke
        2. Mr. Edward Finch
        3. Arnold Gray
        : """)
        if player_input == "1":
            print("")
        elif player_input == "2":
            print("")
        elif player_input == "3":
            print("")
        else:
            print ("Invalid input")

    elif current_room == "4":#Dinning Room
        player_input = input("""Who would you like to question
        1. Mr. Edward Finch
        2. Arnold Gray 
        : """)
        if player_input == "1":
            print("")
        elif player_input == "2":
            print("")
        else:
            print ("Invalid input")

    elif current_room == "5": #Kitchen
        player_input = input("""Who would you like to question
        1. Margaret Holloway
        2. James Thornton
        3. Mr. Edward Finch
        : """)
        if player_input == "1":
            print("")
        elif player_input == "2":
            print("")
        elif player_input == "3":
            print("")
        else:
            print ("Invalid input")

    elif current_room == "6": #Parlor
        player_input = input("""Who would you like to question
        1. Dr Victor Langley
        2. Margaret Holloway
        3. Mr. Edward Finch
        : """)
        if player_input == "1":
            print("")
        elif player_input == "2":
            print("")
        elif player_input == "3":
            print("")
        else:
            print ("Invalid input")

    elif current_room == "7": #Servants' Quarters
        player_input = input("""Who would you like to question
        1. Rebecca Clarke
        2. Arnold Gray
        : """)
        if player_input == "1":
            print("")
        elif player_input == "2":
            print("")
        else:
            print ("Invalid input")

    elif current_room == "8": #Guest Bedrooms
        player_input = input("""Who would you like to question
        1. Dr. Victor Langley
        2. Margaret Holloway
        3. James Thornton
        4. Mr. Edward Finch
        : """)
        if player_input == "1":
            print("")
        elif player_input == "2":
            print("")
        elif player_input == "3":
            print("")
        elif player_input == "4":
            print("")
        else:
            print ("Invalid input")

    elif current_room == "9": #Garden & Greenhouse
        player_input = input("""Who would you like to question
        1. Dr. Victor Langley 
        2. Margaret Holloway
        3. Mr. Edward Finch
        : """)
        if player_input == "1":
            print("")
        elif player_input == "2":
            print("")
        elif player_input == "3":
            print("")
        else:
            print ("Invalid input")

    elif current_room == "10": #Main Bedroom
        player_input = input("""Who would you like to question
        1. Margaret Holloway
        2. Arnold Gray
        : """)
        if player_input == "1":
            print("")
        elif player_input == "2":
            print("")
        else:
            print ("Invalid input")

    elif current_room == "11": #Cellar
        player_input = input("""Who would you like to question
        1. Rebecca Clarke
        2. James Thorton
        : """)
        if player_input == "1":
            print("")
        elif player_input == "2":
            print("")
        else:
            print ("Invalid input")

    else:
        print("Invalid input")

def Guess_culprit(correct):
    player_input = input("""What is your guess
    1. Dr. Victor Langley
    2. Margaret Holloway
    3. James Thornton
    4. Rebecca Clarke
    5. Mr. Edward Finch
    6. Arnold Gray
    : """)
    if player_input == correct:
        print("Correct")
        return False
    else:
        print("Incorrect")

celar_found = False
celar_found = False
current_room = "1"
correct = ""
incorrect = True

print ("On a stormy night, five guests arrive at the secluded Blackwood Manor, invited by the wealthy but enigmatic Lady Eleanor Blackwood. By midnight, Lady Eleanor is found dead in her study, a glass of poisoned wine in her hand. With the storm cutting off all communication, the guests and the loyal butler, Mr. Graves, must uncover the killer before the night is over.")

while incorrect == True:
    player_input = input("""What would you like to do
    1. Move rooms
    2. Search current room
    3. Question suspects
    4. Guess the culprit
    : """)

    if player_input == "1":
        current_room = Move_Room(celar_found, current_room)
    elif player_input == "2":
        Search_room(current_room)
    elif player_input == "3":
        Question_suspect(current_room)
    elif player_input == "4":
        incorrect = Guess_culprit(correct)
    else:
        print("Invalid input")
