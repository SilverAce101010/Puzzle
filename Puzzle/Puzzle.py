def Move_Room(celar_found):
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
        print ("You have moved")
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
        print ("You have moved")
    return player_input

def Search_room():
    player_input = input("Where do you want to search")


def Question_suspect():
    player_input = input("Who would you like to question")

def Guess_culprit():
    player_input = input("""What is your guess
    1. Dr. Victor Langley
    2. Margaret Holloway
    3. James Thornton
    4. Rebecca Clarke
    5. Mr. Edward Finch
    : """)


celar_found = False
print ("On a stormy night, five guests arrive at the secluded Blackwood Manor, invited by the wealthy but enigmatic Lady Eleanor Blackwood. By midnight, Lady Eleanor is found dead in her study, a glass of poisoned wine in her hand. With the storm cutting off all communication, the guests and the loyal butler, Mr. Graves, must uncover the killer before the night is over.")

while True:
    player_input = input("""What would you like to do
    1. Move rooms
    2. Search current room
    3. Question suspects
    4. Guess the culprit
    : """)

    if player_input == 1:
        current_room = Move_Room(celar_found)

    if player_input == 2:
        Search_room(current_room)

    if player_input == 3:
        Question_suspect(current_room)

    if player_input == 4:
        Guess_culprit()
