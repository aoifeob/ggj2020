# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pc = Character("Me")
define r = Character("Rabbit")
define ru = Character("Woman in Purple Shirt")
define t = Character("Tiger")
define tu = Character("Tough-Looking Man")
define m = Character("Monkey")
define mu = Character("Woman with Blue Headband")


# The game starts here.

label start:

    scene bg diningroom

    # These display lines of dialogue.

    "I emerge from the staircase into a brightly-lit, ornately-decorated room."

    " I blink quickly as my eyes take a moment to adjust from the dim lighting of the cellear."

    "Once the bright spots have vanished from my vision, I allow myself to better take in my surroundings."

    "At the centre of the room stands a long wooden table; a row of chairs lining either side. A meek-looking woman in a purple shirt sits at the table, staring quietly down at her hands."

    "If we woman noticed me entering the room, she hasn't given any signs of it."

    "The sound of voices quickly draws my attention away from the woman at the table, towards the end of the room. Two people are standing near a large mahogany door, their faces animated as they speak."

    show tiger

    "tu" "We'll never reach it. There has to be another way through that door, something we haven't tried yet."
    # This ends the game.

    return
