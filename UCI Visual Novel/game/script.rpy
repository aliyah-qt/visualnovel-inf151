# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# MC stands for main character
define MC = Character("[name]")

define p = Character("Peter The Anteater")
image peter_left_default = im.Scale("images/anteater_left_default.png", 600, 600)
image peter_left_evil = im.Scale("images/anteater_left_evil.png", 600, 600)
image peter_right_evil = im.Scale("images/anteater_right_evil.png", 600, 600)

define j = Character("Jason")
image jason_fear = im.Scale("images/support_male_left_fear.png", 660, 660)
image jason_poker = im.Scale("images/support_male_left_poker.png", 660, 660)
image jason_default = im.Scale("images/support_male_left_default.png", 660, 660)

define viv = Character("Vivian")
image vivian_fear = im.Scale("images/support_female_right_fear.png", 660, 660)
image vivian_default = im.Scale("images/support_female_right_default.png", 660, 660)
image vivian_poker = im.Scale("images/support_female_right_poker.png", 660, 660)

image fao = im.Scale("images/aldrich_hall.jpg", 1300, 900)
image bedroom = im.Scale("images/bedroom.jpg", 1300, 800)
image gym = im.Scale("images/athletics_center_inside.jpg", 1300, 800)
image bren = im.Scale("images/bren_events_center_temp.jpg", 1300, 800)
image map = im.Scale("images/UCI_campus_map.jpg", 1300, 800)

# The game starts here.

label start:

    python:
        name = renpy.input("What's your name?")

        name = name.strip() or "Me"

    stop music fadeout 1.0

    scene bedroom
    with fade

    # Start of MC internal dialogue

    "Finally, it's orientation day! This will mark the beginning of my new
    journey at UCI."

    "I should be heading to Bren Events Hall. That's where the event is
    supposed to take place."

    scene gym
    with fade

    "Here I am. Well, the building doesn't look so bad."

    "Why are there only 3 other students here? Did I mess up the time and
    location, or did I arrive early?"

    # optional description and/or thought about each supporting character

    "Come to think of it, when was the last time I arrived early for an event?"

    "Hm..."

    # italics represents the main character's (MC) action(s)
    "{i}You pull out your phone to recheck the orientation email but just as
    quickly put it away{/i}"

    "No, this is the correct time and place. The orientation should be starting
    soon. Maybe I should wait a few more minutes."

    show peter_left_default at left

    "Huh? Are we supposed to cosplay for orientation?"

    p "Hello to all the new students and welcome to UCI Student Orientation 2021!"

    show peter_left_evil at left

    p "I am Peter The Anteater, the leader of the anteaters, and we have taken over UCI."

    p "We have used our ant-algorithms and paired you with two more incoming students
       who will be a part of your quest today."

    p "We sincerely hope you enjoy and complete the first ever challenge you face
       at UCI."

    p "If you fail...you're not allowed back to UCI!"

    p "You all have been sent the rules and objectives for today's quest on your devices.
       Good luck!"

    hide peter_left_default
    hide peter_left_evil

    "As Peter The Anteater leaves, a very audible noise follows."

    "{i}Zot...Zot...Zot...{/i}"

    "Well, does that mean if I fail to pass the test, my dream of going to one of
    the best universities in California will end?"

    "I can't let that happen. I'll have to team up with the other students here.
    Although, I'm not sure if they'd want to work together as a team."

    MC "Hey! Do any of you want to work together? I am sure the university's
    academic integrity policy does not cover this."

    show jason_fear at left

    j "I was about to say the same thing!"

    show vivian_fear at right

    viv "Yes! Let's work together to figure this out."

    MC "Alright, let's head out."

    scene bren
    with fade

    show jason_poker at left
    show vivian_default at right

    viv "According to the Peter The Anteater, we're supposed to pass
    {b}4 tests{/b} at {b}4 different locations{/b}."

    j "Let's check out the map."

    scene map
    with dissolve

    j "Where should we go first?"

    MC "Let's head to the Financial Aid Office."

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

    show jason_default at left
    show vivian_default at right

    MC "Here we are."

    j "Hm...there's no one around."

    viv "I guess the anteaters really did take control of everything."

    MC "Let's look around for information. We may find what we need on those
    catalogues and flyers."

    j "Yes, we can split up. [name] and I will take this floor while Vivian
    takes the other floor."

    show vivian_fear at right

    viv "What if I run into one of those anteaters?"

    j "Then just run back to us."

    show vivian_poker at right

    viv "Easy for you to say..."

    MC "Let's get to work."

    hide vivian_default
    hide vivian_fear
    hide vivian_poker
    #show inside of financial aid building
    # show jason_default at right

    MC "Check this out. Apparently you're supposed to pay your tuition here. I guess
    you'll come back to this building after all, Mr. Self Sufficient."

    j "Heh. Fine by me."

    j "{b}So you're supposed to pay all your fees even before the first day of school,
    otherwise your classes will get dropped.{/b} How about that?"

    MC "Hehe. FAFSA got my back. I don't have to worry about paying on time since
    they automatically pay for me, you know."

    j "Wow, that's very nice of them. I wonder if I'm eligible for aid if I apply."

    "{i}You turn to Jason with a wide smirk on your face{/i}"

    MC "What's wrong Jason? You don't feel self-sufficient anymore?"

    j "I can be in need and self-sufficient at the same time, you know?"

    MC "Sure. Quick tip: If you have to ask if you qualify, you probably don't."

    j "How do they determine if I'm eligible for aid or not?"

    MC "Oh, I found it here! Basically all you have to do is apply for it using
    the MyAid section at {a=https://www.ofas.uci.edu/index.php}https://www.ofas.uci.edu/{/a}"

    MC "They will automatically determine whether you qualify for financial aid."

    j "Heh. Sounds simple enough."

    MC "Look at this. You don't even have to enroll full-time to receive aid."

    j "Interesting. Even though we're supposed to pay less for part time enrollment,
    right?"

    # need to figure out how to display 50%
    MC "Yes. Looks like{b}you only pay half the price for a maximum of 10 units
    of undergraduate courses and 8 units of graduate courses{/b}."

    j "That sounds reasonable."

    MC "Wait, what if we only do part time study? If I can't afford to take the
    maximum of 20 units every term, would going part-time maximize the cost per
    unit for me?"

    j "Errr...I think you're right."

    MC "So what's stopping us?"

    j "I guess we can all do that if we're not planning on graduating in four years."

    MC "Yeah. Time is money. Who would've thought..."

    j "Anyways, just remember to {b}apply for FAFSA by March 2nd for the next academic yearself."

    j "But I guess you already know that since you're here now."

    "{i}You let out a loud laugh{/i}"

    MC "I don't."

    j "Not you..."

    "{i}You and Jason continue searching through the office to find more information.{/i}"

    MC "I think we got all the basic information from this building. Let's move
    onto the next building."

    j "Sounds good to me! Let's check out the map."

#    "{i}Eeeeeeeppp!{/i}"

#    "{i}You and Jason look at each other in fear before running towards the door{/i}"

#    show vivian_fear at left

#    viv "A- An-"

#    MC "I don't understand."

#    j "Spit it out Vivian!"

#    viv "Peter The Anteater is on the top floor."

#    MC "Did he say what he wants?"

#    "{i}Vivian shakes her head while her eyes remain focused on the stairwell from which she came{/i}"

#    viv "I was exploring the Registrar Office and he just appeared out of no where."

#    j "I'm just going to have to get it out of him then!"

#    hide jason_default

#    "{i}Before you know it, Jason quickly charges up the stairwell leaving you and Vivian behind{/i}"

#    viv "Wait, Jason!"

#    hide vivian_fear

#    "{i}Vivian runs after him leaving you all alone{/i}"

#    "Well, I'm not going to just stay here by myself."

#    "{i}You follow the rest of your team not knowing what to expect{/i}"

#    "{i}Once you reach the top of the stairwell, you see Jason with his eyes closed on the floor,
#    and Vivian who looks like she's about to pee her pants.{/i}"

#    "{i}You move your eyes to the figure immediately in front of her, Peter The Anteater,
#    who looks as evil as ever{/i}"

    show peter_right_evil at right
    show jason_fear at left

    p "Not so fast! I hope you discovered some useful information because it's
    QUIZ TIME!"

    p "Pass the quiz with a 75%% or higher and you're free to continue
    exploring campus."

    p "But if you don't pass...let's just say there will be some consequences."

    "{i}You turn to look at Jason who is visibly shaking with fear{/i}"

    "{i}You let out a big gulp as you feel the pit of your stomach get heavy{/i}"

    p "Let's begin!"

    hide jason_default
    hide jason_fear

    #start of quiz 1
    menu:

#        default result = False

        #question 1
        "When is the deadline to pay for your classes?"

        "Depends on the term, but it is always before the first day of class":
#            $ result = True
            jump question2

        "First day of class":
            jump question2

        "Before the end of the second week of class":
            jump question2

        "Before taking the finals":
            jump question2

label question2:

    menu:

        #question 2
        "How do you apply for financial aid?"

        "Trick question, we don’t. Financial aid is awarded automatically":
            jump question3

        "Apply from MyAid section at {a=https://www.ofas.uci.edu/index.php}https://www.ofas.uci.edu/{/a}":
            jump question3

        "Talk to staff at the financial aid office":
            jump question3

        "Talk to your tax prep specialist":
            jump question3

label question3:

    menu:

        #question 3
        "What is the requirement to receive financial aid?"

        "Be enrolled full-time":
            jump question4

        "You don’t need to be a full time student to receive financial aid":
            jump question4

        "Be a member of the students’ government":
            jump question4

        "Have a 3.5 GPA":
            jump question4

label question4:

    menu:

        #question 4
        "If you decide to become a part time student, the limitation is:"

        "50%% tuition for a maximum of 6 units of undergrad, 4 units of graduate classes":
            jump question5

        "50%% tuition for a maximum of 10 units of undergrad, 8 units of graduate classes":
            jump question5

        "75%% tuition for a maximum of 9 units of undergrad, 6 units of graduate classes":
            jump question5

        "75%% tuition for a maximum of 10 units of undergrad, 8 units of graduate classes":
            jump question5

label question5:

    menu:

        #question 5
        "When is the deadline to apply for FAFSA?"

        "March 2nd of the previous academic year":
            jump result

        "March 2nd of the current academic year":
            jump result

        "February 3 of the previous academic year":
            jump result

        "February 3 of the current academic year":
            jump result

label result:

    p "The result of your quiz is..."

    # This ends the game.

    return
