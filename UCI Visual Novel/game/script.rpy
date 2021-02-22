# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# MC stands for main character
define MC = Character("[name]")

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

    python:
        name = renpy.input("What's your name?")

        name = name.strip() or "Me"

    stop music fadeout 1.0

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

    "{i}Vivian turns to look at me with a curious look in her eyes{/i}"

    viv "[name], do you need any scholarships?"

    MC "Yeah. But if I don't get it, will I ever visit this building again?"

    viv "Hm...I wonder how many scholarships they hand out in a year."

    j "I hope we'll find more information there..."

   # fao stand for financial aid office
    scene fao
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show jason at left
    show vivian at right

    # These display lines of dialogue.

    MC "Here we are."

    j "Hm...there's no one around."

    viv "I guess the robots really took control of everything."

    MC "Let's look around for information. We may find what we need on those
    catalogues and flyers."

    viv "Yes, we can split up. Jason and I will take this floor while [name] and
    OTHER SUPPORTING CHARACTER take the other floor."

    j "Sure, let's get to work."

    # some stuff happens here

    j "Check this out! You are supposed to pay your tuition here too. I guess
    you will come back to this building after all, Mr/Ms SelfSufficient."

    MC "Heh. Fine by me."

    viv "{b}So you're supposed to pay all your fees even before the first day of school,
    otherwise your classes will get dropped.{/b} How about that?"

    # other supporting character "Hehe. FAFSA got my back. I don't have to worry
    # about paying on time you know"

    MC "Wow, that's very nice of tem. I wonder if I am eligible for aid if I apply."

    "{i}Jason turns to you with a wide smirk on his face{/i}"

    j "What's wrong [name]? You don't feel self-sufficient anymore?"

    MC "I can be in need and self-sufficient at the same time you know?"

    j "Sure. Quick tip: If you have to ask if you qualify, you probably don't."

    MC "By the way, how do they determine if I am eligible for aid or not?"

    viv "Oh, I found it here! Basically all you have to do is apply for it using
    the MyAid section at {a=https://www.ofas.uci.edu/index.php}https://www.ofas.uci.edu/{/a}"

    viv "They will automatically determine whether you qualify for financial aid."

    j "That sounds simple enough."

    viv "Look at this. You don't even have to enroll full-time to receive aid."

    j "Interesting. Even though we're supposed to pay less for part time enrollment,
    right?"

    # need to figure out how to display 50%
    viv "Yes. Looks like{b}you only pay half the price of a maximum of 10 units
    of undergraduate courses, and 8 units of graduate courses{/b}."

    MC "That sounds reasonable."

    j "Wait, what if we only do part time study? If I cannot afford to take the
    maximum of 20 units every term, would going part-time maximize the cost per
    unit for me?"

    viv "Errr...I think you are right."

    MC "So what is stopping us?"

    # This ends the game.

    return
