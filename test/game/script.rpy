# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jason")
image jason = im.Scale("images/support_male_jason.png", 660, 660)

image fao = im.Scale("images/aldrich_hall.jpg", 1300, 900)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene fao

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show jason at left

    # These display lines of dialogue.

    j "My name is Jason."

    j "I am one of the supporting male characters in your visual novel inputted by Aliyah."

    j "See you real soon!"

    # This ends the game.

    return
