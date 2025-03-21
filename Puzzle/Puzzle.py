import random

def Move_Room(current_room):
    player_input = input("""
    Which room would you like to move to
    1. Grand Hall
    2. Study
    3. Library
    4. Dining Room
    5. Kitchen
    6. Parlor
    7. Servants' Quarters
    8. Guest Bedrooms
    9. Garden & Greenhouse
    10. Main Bedroom
    11. Cellar
    : """)
    if player_input == "":
        print("You have not moved")
        player_input = current_room
    else:
        print("You have moved")
    return player_input

rooms = {
    "1": {"name": "Grand Hall", "clues": [
        "A shattered wine glass lies near the fireplace.", "A torn piece of fabric is caught on a chair.", "A strange perfume lingers in the air.", "A small puddle of water near the entrance.", "A muddy footprint leading towards the Study.", "A faint scratch mark on the wooden floor.", "A flickering chandelier with a broken bulb.", "A piece of paper with half-burnt writing.", "A glove that doesn’t belong to the staff.", "A strange indentation in the rug."]},
    "2": {"name": "Study", "clues": [
        "A diary with missing pages is on the desk.", "A safe is slightly ajar, revealing some missing documents.", "A pen with dried ink, as if hastily put down.", "A chair positioned awkwardly, as if someone left in a hurry.", "A shattered ink bottle on the floor.", "A hidden compartment in the bookshelf.", "A burnt matchstick near the fireplace.", "A window slightly open despite the storm.", "A glass with lipstick stains.", "A note addressed to someone named 'M'."]},
    "3": {"name": "Library", "clues": [
        "Burned book pages are scattered on the floor.", "A chair is knocked over, as if there was a struggle.", "A missing book titled 'The Secrets of Blackwood'.", "A candle melted down completely.", "A strong scent of tobacco lingers.", "A bookmark with initials 'J.T.' on it.", "A ledger detailing significant debts.", "A curtain torn at the edges.", "A hidden panel in the wall.", "A faded photograph of Lady Eleanor."]},
    "4": {"name": "Dining Room", "clues": [
        "A half-eaten meal is left abandoned.", "A candlestick with dried blood on it is missing from the holder.", "A shattered plate beneath the table.", "A folded napkin with a cryptic message.", "A wine bottle with an unfamiliar label.", "A chair slightly pulled back as if someone left quickly.", "A faint handprint on the window.", "A key left under the table.", "A scuff mark on the wall near the entrance.", "A faint scent of lavender."]},
    "5": {"name": "Kitchen", "clues": [
        "A broken bottle of poison lies near the sink.", "A knife is missing from the cutlery set.", "An apron with fresh stains.", "A cupboard slightly ajar.", "A set of muddy footprints leading to the back door.", "A torn recipe page in the trash.", "A wine glass with smudged fingerprints.", "A bundle of letters tied with a red ribbon.", "A matchbox with only one match left.", "A clock stopped at exactly midnight."]},
    "6": {"name": "Parlor", "clues": [
        "An overturned tea cup with lipstick stains.", "A hidden compartment in the piano.", "A poker game in progress, but abandoned.", "A strong smell of cigars.", "A broken picture frame.", "A stack of unpaid bills.", "A half-written letter left on the desk.", "A velvet glove under the couch.", "A glass of whiskey, untouched.", "A watch stopped at 11:45 PM."]},
}

suspects = {
    "1": "Dr. Victor Langley – A brilliant but disgraced scientist with a history of financial trouble.",
    "2": "Margaret \"Maggie\" Holloway – Lady Eleanor’s estranged niece, desperate for an inheritance.",
    "3": "James Thornton – A charming but debt-ridden gambler with ties to the victim.",
    "4": "Rebecca Clarke – A loyal housekeeper who knows all the family secrets.",
    "5": "Mr. Edward Finch – A reserved lawyer who recently altered Lady Eleanor’s will."
}

statements = {
    "Dr. Victor Langley": [
        "I was in the Study all evening, going through old medical records.", "I had no reason to harm Lady Eleanor. She funded my research when no one else would.", "I heard footsteps outside the Study.", "Lady Eleanor recently cut my funding.", "I saw James arguing with her earlier.", "Someone tampered with my research notes.", "The library lights were flickering last night.", "A bottle of my sleeping tonic is missing.", "I found a strange note on my desk.", "Margaret seemed unusually nervous.", "Lady Eleanor called me to discuss something urgent.", "Rebecca seemed to be hiding something.", "Someone spilled ink over some important documents.", "The safe was already open when I checked it.", "I heard a loud noise from the Parlor before midnight."],
    "Margaret \"Maggie\" Holloway": [
        "I was in the garden when the storm started.", "Lady Eleanor always treated me unfairly, but I would never harm her.", "I was hoping to reconcile with her before this happened.", "I don't know why, but I found the letter from the lawyer strange.", "I overheard Rebecca talking to someone about secrets in the house.", "I heard footsteps in the hallway during the night.", "James was always pressuring Lady Eleanor for money.", "I found the inheritance terms to be quite cruel.", "I never trusted Dr. Langley. He's hiding something.", "I was in the Kitchen earlier, preparing some tea.", "I knew about Lady Eleanor's plan to change the will.", "I often argued with Lady Eleanor about her neglecting me.", "I saw someone outside my bedroom window just before midnight.", "The family portrait in the hall was strangely tilted.", "The sound of the piano stopped abruptly last night."],
    "James Thornton": [
        "I was gambling in the Parlor when the incident happened.", "Lady Eleanor and I had an argument earlier that night.", "I never borrowed money from her, though she often hinted I should.", "I saw Dr. Langley leave the Library in a hurry.", "Rebecca has always been protective of the family secrets.", "I was close to Lady Eleanor before her sudden coldness.", "I heard strange noises coming from the Cellar late at night.", "I knew Lady Eleanor was planning to change her will, but I didn't know the details.", "I saw Maggie leave the house in the middle of the night.", "I was in the Study earlier, trying to get my finances in order.", "Someone had been rummaging through my gambling debts.", "I had nothing to do with Lady Eleanor's death.", "The cellar door was open when I passed by.", "The clock in the Dining Room had stopped right at midnight.", "I often used to play cards with Lady Eleanor before she grew distant."],
    "Rebecca Clarke": [
        "I was cleaning the Study when I heard a loud noise.", "Lady Eleanor trusted me more than anyone else in this house.", "I found strange footprints leading to the Parlor.", "James was gambling again when he should have been focusing on more important matters.", "I overheard a conversation between Lady Eleanor and Maggie.", "I know all of Lady Eleanor’s secrets, but I would never betray her.", "There was a strange letter in the Dining Room earlier.", "I found a broken vase in the hallway near the main stairs.", "I was in the kitchen when I heard a scream.", "I often stayed up late to ensure the house was in order.", "Someone left a strange key on the floor near the Cellar.", "I’ve seen Maggie’s temper flare before; she could be dangerous.", "Dr. Langley often muttered to himself about unfinished work.", "I noticed that the Parlor had been disturbed last night.", "The piano in the Parlor was off-key, as if someone had been playing it hurriedly."],
    "Mr. Edward Finch": [
        "I was in the Study reviewing legal documents.", "Lady Eleanor's will was about to be changed, but I didn't know who would benefit.", "I altered the will, but it was with Lady Eleanor's consent.", "I saw James leave the Library in a hurry, but he was acting strange.", "Maggie seemed eager to discuss family matters earlier that night.", "I overheard a heated argument between Dr. Langley and Lady Eleanor.", "I found a piece of paper with a strange symbol in the study.", "The garden gate was left slightly ajar last night.", "I heard muffled voices in the hallway after midnight.", "I don’t know why, but I feel like I’m being watched.", "I always had a professional relationship with Lady Eleanor.", "I’ve seen Rebecca cleaning the Parlor at odd hours.", "I’ve been in and out of the house during the night, reviewing the legal matters.", "There was a faint smell of cigar smoke near the study window.", "I found a letter in the Library addressed to someone named 'T'."]   
}

suspect_details = {
    "Dr. Victor Langley": "A disgraced scientist who was once funded by Lady Eleanor. Recently, she cut his research funding, leaving him desperate.",
    "Margaret \"Maggie\" Holloway": "Lady Eleanor’s estranged niece, hoping for an inheritance. She had a rocky relationship with her aunt.",
    "James Thornton": "A gambler drowning in debt. Lady Eleanor refused to help him financially, leading to bitter arguments.",
    "Rebecca Clarke": "The housekeeper who knows the family's darkest secrets. Loyal to Lady Eleanor, but perhaps hiding something.",
    "Mr. Edward Finch": "A reserved lawyer who recently altered Lady Eleanor’s will. Could his changes have put someone at risk?"
}

murderer = random.choice(list(suspects.values()))

# Initialize tracking of clues and statements
suspects_questioned = {
    "Dr. Victor Langley": [],
    "Margaret \"Maggie\" Holloway": [],
    "James Thornton": [],
    "Rebecca Clarke": [],
    "Mr. Edward Finch": []
}

# Initialize tracking of clues and statements
clues_found = {
    "1": [], "2": [], "3": [], "4": [], "5": [], "6": []  # Tracks clues found in each room
}

all_clues_found = []  # All clues found throughout the game

suspects_questioned = {
    "Dr. Victor Langley": [],
    "Margaret \"Maggie\" Holloway": [],
    "James Thornton": [],
    "Rebecca Clarke": [],
    "Mr. Edward Finch": []
}

all_statements_heard = []  # All statements heard throughout the game

def View_progress(current_room):
    print("\n--- Progress so far ---")
    
    # View all clues found throughout the game
    print("\nClues found throughout the game:")
    if all_clues_found:
        for clue_info in all_clues_found:
            print(f"- {clue_info['clue']} (Found in {clue_info['room']})")
    else:
        print("No clues have been found yet.")
    
    # View all statements heard throughout the game
    print("\nStatements heard from suspects:")
    if all_statements_heard:
        for statement_info in all_statements_heard:
            print(f"- {statement_info['statement']} (From {statement_info['suspect']})")
    else:
        print("No statements have been heard yet.")

def Search_room(current_room):
    room = rooms.get(current_room, None)
    if room:
        print(f"\nYou are in the {room['name']}.")
        remaining_clues = [clue for clue in room["clues"] if clue not in clues_found[current_room]]
        
        if remaining_clues:
            # Randomly select one clue from the remaining clues
            clue = random.choice(remaining_clues)
            print(f"Clue found: {clue}")
            clues_found[current_room].append(clue)
            # Track the clue with the room it was found in
            all_clues_found.append({"clue": clue, "room": room['name']})
        else:
            print("You have found all the clues in this room.")
    else:
        print("Invalid room.")

def Question_suspect():
    print("""
    Who would you like to question?
    """)
    for key, suspect in suspects.items():
        print(f"{key}. {suspect}")
    player_input = input(": ")
    if player_input in suspects:
        suspect_name = suspects[player_input].split(" – ")[0]
        
        # Check if all statements have been heard for this suspect
        remaining_statements = [statement for statement in statements[suspect_name] if statement not in suspects_questioned[suspect_name]]
        
        if remaining_statements:
            # Randomly select one of the remaining statements
            statement = random.choice(remaining_statements)
            print(f"{suspect_name} says: \"{statement}\"")
            suspects_questioned[suspect_name].append(statement)
            # Track the statement with the suspect's name
            all_statements_heard.append({"statement": statement, "suspect": suspect_name})
        else:
            print(f"You have heard all the statements from {suspect_name}.")
    else:
        print("Invalid suspect.")

def View_suspect_info():
    print("\n--- Suspect Information ---")
    for key, suspect in suspects.items():
        print(f"{key}. {suspect}")
    player_input = input("\nSelect a suspect to view details: ")
    if player_input in suspects:
        suspect_name = suspects[player_input].split(" – ")[0]
        print(f"\n--- {suspect_name} ---")
        print(f"{suspect_details[suspect_name]}")
    else:
        print("Invalid choice.")

def Guess_culprit():
    print("Who do you think the murderer is?")
    for key, suspect in suspects.items():
        print(f"{key}. {suspect}")
    player_input = input(": ")
    if player_input in suspects and suspects[player_input] == murderer:
        print("Correct! You solved the mystery.")
        return False
    else:
        print("Incorrect! Keep investigating.")
        return True

incorrect = True
current_room = "1"
print("On a stormy night, five guests arrive at the secluded Blackwood Manor only to find thier host Lady Eleanor dead in the morning...")

while incorrect:
    player_input = input("""
    What would you like to do?
    1. Move rooms
    2. Search current room
    3. Question suspects
    4. Guess the culprit
    5. View progress (clues & statements)
    6. View suspect info
    : """)
    if player_input == "1":
        current_room = Move_Room(current_room)
    elif player_input == "6":
        View_suspect_info()
    elif player_input == "4":
        incorrect = Guess_culprit()
    else:
        print("Invalid input")
