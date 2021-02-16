# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define MC = Character("Main Character")

define j = Character("Jason")
image jason = im.Scale("images/jason.png", 660, 660)

define viv = Character("Vivian")
image vivian = im.Scale("images/vivian.png", 660, 660)

define rob = Character("Robot")
# need to insert image once available

image fao = im.Scale("images/aldrich_hall.jpg", 1300, 900)
image bedroom = im.Scale("images/bedroom_temp.jpg", 1300, 800)
image gym = im.Scale("images/athletics_center_inside.jpg", 1300, 800)
image bren = im.Scale("images/bren_events_center_temp.jpg", 1300, 800)
image map = im.Scale("images/UCI_campus_map.jpg", 1300, 800)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bedroom
    with fade

    # MC dialogue

    "Finally, it's orientation day! This will mark the beginning of my new
    journey at UCI."

    "I should be heading to Bren Events Hall. That's where the event is
    supposed to start."

    scene gym
    with fade

    "Here I am. Well, the building does not look so bad."

    "Why are there only 3 other students here? Did I mess up the time and
    location, or did I arrive early?"

    # optional description and/or thought about each supporting character

    "Come to think of it, when was the last time I arrived early for an event?"

    "Hm..."

    # italics represents the main character's (MC) action(s)
    "{i}You pull out your phone to recheck the orientation email{/i}"

    "No, this is the correct time and place. The orientation should be starting
    soon. Maybe I should wait a few more minutes."

    #show rob at right

    "Huh? Are we supposed to cosplay for orientation?"

    #Robot's dialogue
    # to be filled out

    "Well, does that mean if I fail to pass the test, my dream of going to one of
    the best universities in California will end?"

    "I can't let that happen. I'll have to team up with the other students here.
    Although, I'm not sure if they'd want to work together as a team."

    rob "You don't have an option."

    MC "Hey guys! Do any of you want to work together? I am sure the university's
    academic integrity policy does not cover this!"

    show jason at left

    j "I'm in!"

    show vivian at right

    viv "Me too!"

    #more dialogue between characters

    MC "Alright, let's head out."

    scene bren
    with fade

    #show jason at left
    #show vivian at right

    MC "According to the robot, we are supposed to pass {b}6 tests{/b} at {b}6 different locations{/b}."

    MC "Let's check out the map."

    scene map
    with dissolve

    MC "Where should we go first?"

    # insert more dialogue here later

    MC "Sure, let's head to the Financial Aid Office."

    j "But what if I don't need any aid. Do they provide any other services for me?"

    viv "I think they do. The full name of the UCI building is: The Office of
    Financial Aid and Scholarships."

    "Vivian turns to look at me with a curious look in her eyes"

    viv "Do you need any scholarships?"

    MC "Yeah. But if I don't get it, will I ever visit this building again?"

    viv "Hm...I wonder how many scholarships they hand out in a year."

    j "I hope we'll find more information there..."

######
#    scene fao
#     with fade
    # fao stand for financial aid office

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

#    show jason at left

    # These display lines of dialogue.

#    j "My name is Jason."

#    j "I am one of the supporting male characters in your visual novel inputted by Aliyah."

#    j "See you real soon!"


    # This ends the game.

    return
