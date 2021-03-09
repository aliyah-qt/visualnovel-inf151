# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# MC stands for main character
define MC = Character("[name]")


define p = Character("Peter The Anteater")
image peter_left_default = im.Scale("images/anteater_left_default.png", 600, 600)
image peter_left_evil = im.Scale("images/anteater_left_evil.png", 600, 600)
image peter_left_happy = im.Scale("images/anteater_left_happy.png", 600, 600)

image peter_right_default = im.Scale("images/anteater_right_default.png", 600, 600)
image peter_right_evil = im.Scale("images/anteater_right_evil.png", 600, 600)
image peter_right_happy = im.Scale("images/anteater_right_happy.png", 600, 600)


define j = Character("Jason")
image jason_left_fear = im.Scale("images/support_male_left_fear.png", 660, 660)
image jason_left_poker = im.Scale("images/support_male_left_poker.png", 660, 660)
image jason_left_default = im.Scale("images/support_male_left_default.png", 660, 660)
image jason_left_happy = im.Scale("images/support_male_left_happy.png", 660, 660)
image jason_left_excited = im.Scale("images/support_male_left_excited.png", 660, 660)

image jason_right_fear = im.Scale("images/support_male_right_fear.png", 660, 660)
image jason_right_poker = im.Scale("images/support_male_right_poker.png", 660, 660)
image jason_right_default = im.Scale("images/support_male_right_default.png", 660, 660)
image jason_right_happy = im.Scale("images/support_male_right_happy.png", 660, 660)
image jason_right_excited = im.Scale("images/support_male_right_excited.png", 660, 660)


define viv = Character("Vivian")
image vivian_left_fear = im.Scale("images/support_female_left_fear.png", 660, 660)
image vivian_left_default = im.Scale("images/support_female_left_default.png", 660, 660)
image vivian_left_poker = im.Scale("images/support_female_left_poker.png", 660, 660)
image vivian_left_excited = im.Scale("images/support_female_left_excited.png", 660, 660)
image vivian_left_happy = im.Scale("images/support_female_left_happy.png", 660, 660)

image vivian_right_fear = im.Scale("images/support_female_right_fear.png", 660, 660)
image vivian_right_default = im.Scale("images/support_female_right_default.png", 660, 660)
image vivian_right_poker = im.Scale("images/support_female_right_poker.png", 660, 660)
image vivian_right_excited = im.Scale("images/support_female_right_excited.png", 660, 660)
image vivian_right_happy = im.Scale("images/support_female_right_happy.png", 660, 660)

image aldrich = im.Scale("images/aldrich_hall.jpg", 1300, 900)
image fao = im.Scale("images/fao.PNG", 1300, 900)
image bedroom = im.Scale("images/bedroom.jpg", 1300, 800)
image gym = im.Scale("images/athletics_center_inside.jpg", 1300, 800)
image bren = im.Scale("images/bren_events_center_temp.jpg", 1300, 800)
image map = im.Scale("images/UCI_campus_map.jpg", 1300, 800)
image ring_road = im.Scale("images/ring_road.jpg", 1300, 900)
image gateway = im.Scale("images/gateway_study_center.jpg", 1300, 900)
image langson = im.Scale("images/langson.jpg", 1300, 900)
image bus = im.Scale("images/bus.jpg", 1300, 900)
image ARC_outside = im.Scale("images/ARC_outside.jpg", 1300, 900)
image ARC_inside1 = im.Scale("images/ARC_inside1.png", 1300, 900)
image ARC_inside2 = im.Scale("images/ARC_inside2.png", 1300, 900)
image black_screen = im.Scale("images/black_screen.png", 1300, 900)
image registrar = im.Scale("images/registrar.jpg", 1300, 900)

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

    show jason_left_fear at left

    j "I was about to say the same thing!"

    show vivian_right_fear at right

    viv "Yes! Let's work together to figure this out."

    MC "Alright, let's head out."

    scene bren
    with fade

    show jason_left_poker at left
    show vivian_right_default at right

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

    scene aldrich
    with fade

    show jason_left_default at left
    show vivian_right_default at right

    MC "Here we are."

    j "Hm...there's no one around."

    viv "I guess the anteaters really did take control of everything."

    MC "Let's look around for information. We may find what we need on those
    catalogues and flyers."

    j "Yes, we can split up. [name] and I will take the lower floor while Vivian
    takes the top floor."

    show vivian_right_fear at right

    viv "What if I run into one of those anteaters?"

    j "Then just run back to us."

    show vivian_right_poker at right

    viv "Easy for you to say..."

    MC "Let's get to work."

    hide vivian_right_default
    hide vivian_right_fear
    hide vivian_right_poker

    scene fao
    with fade

    show jason_left_default at left

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

    MC "Yes. Looks like{b}you only pay 50%% for a maximum of 10 units
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
    show jason_left_fear at left

    p "Not so fast! I hope you discovered some useful information because it's
    QUIZ TIME!"

    p "Pass the quiz with a 75%% or higher and you're free to continue
    exploring campus."

    p "But if you don't pass...let's just say there will be some consequences."

    "{i}You turn to look at Jason who is visibly shaking with fear{/i}"

    "{i}You let out a big gulp as you feel the pit of your stomach get heavy{/i}"

    p "Let's begin!"

    hide jason_left_default
    hide jason_left_fear

# start of quiz 1
label q1q1:

    $ q1result = 0

    menu:

        #question 1
        "When is the deadline to pay for your classes?"

        "Depends on the term, but it is always before the first day of class":
            $ q1result += 1
            jump q1q2

        "First day of class":
            jump q1q2

        "Before the end of the second week of class":
            jump q1q2

        "Before taking the finals":
            jump q1q2

label q1q2:

    menu:

        #question 2
        "How do you apply for financial aid?"

        "Trick question, we don’t. Financial aid is awarded automatically":
            jump q1q3

        "Apply from MyAid section at: www.ofas.uci.edu":
            $ q1result += 1
            jump q1q3

        "Talk to staff at the financial aid office":
            jump q1q3

        "Talk to your tax prep specialist":
            jump q1q3

label q1q3:

    menu:

        #question 3
        "What is the requirement to receive financial aid?"

        "Be enrolled full-time":
            jump q1q4

        "You don’t need to be a full time student to receive financial aid":
            $ q1result += 1
            jump q1q4

        "Be a member of the students’ government":
            jump q1q4

        "Have a 3.5 GPA":
            jump q1q4

label q1q4:

    menu:

        #question 4
        "If you decide to become a part time student, the limitation is:"

        "50%% tuition for a maximum of 6 units of undergrad, 4 units of graduate classes":
            jump q1q5

        "50%% tuition for a maximum of 10 units of undergrad, 8 units of graduate classes":
            $ q1result += 1
            jump q1q5

        "75%% tuition for a maximum of 9 units of undergrad, 6 units of graduate classes":
            jump q1q5

        "75%% tuition for a maximum of 10 units of undergrad, 8 units of graduate classes":
            jump q1q5

label q1q5:

    menu:

        #question 5
        "When is the deadline to apply for FAFSA?"

        "March 2nd of the previous academic year":
            jump q1result

        "March 2nd of the current academic year":
            $ q1result += 1
            jump q1result

        "February 3 of the previous academic year":
            jump q1result

        "February 3 of the current academic year":
            jump q1result

label q1result:

    p "The result of your quiz is..."

    p "%(q1result)s out of 5. Which means..."

    if q1result >= 4:

        show peter_right_happy at right

        p "YOU PASSED!"

    else:

        p "You failed."

        p "As per UCI policy, I will forget your current score if you receive a
        passing score for this retake quiz."

        p "Which starts now!"

        jump q1q1

    hide peter_right_happy
    show peter_right_evil at right

    p "You were successful this time, but will you be for the future quizzes?"

    p "See you real soon!"

    hide peter_right_evil

    show jason_left_default at left

    j "I'm glad that's over!"

    MC "We should check on Vivian."

    "{i}You and Jason ascend up the stairwell{/i}"

    scene registrar
    with fade

    show vivian_right_default at right

    "{i}At the top of the stairwell, you notice Vivian standing near a window called
    The Registrar Office{/i}"

    show jason_left_default at left

    j "Here we are. Apparently this is the office that deals with class registration."

    viv "That sounds important."

    MC "Yeah, we're here to take classes right? Or do we?"

    j "Yeah, we sure are."

    MC "Alright, let’s see what we have here."

    viv "It seems that {b}the deadline to drop a class without a ‘W’ on your transcript
    is the end of the 2nd week of instruction.{/b}"

    j "Is a ‘W’ a bad thing? It stands for ‘Withdrawal’ right?"

    MC "Yes. Withdrawal. It doesn't count towards your GPA. But if you have a ‘W’,
    people might think that you cannot handle the class, and you don’t want to take
    an ‘F’ or ‘D’ grade either."

    viv "That’s right. Having many ‘W’s on your transcript will definitely make you look bad."

    j "But your GPA only affects you if you plan on going for graduate school right?"

    viv "Oh, that’s right. But I guess employers only look at your overall GPA.
    They only request a transcript if they hire you."

    j "Don’t forget that if you drop too many classes, you will also delay your
    own graduation. If anything, you should be trying to maximize your classes
    because you pay a fixed price for it."

    MC "Speaking of which, how many classes are we allowed to take per term?"

    viv "Oh I know this! {b}You are allowed a maximum of 20 units per quarter. If
    you want to add more units, you would have to talk to your academic advisor
    about that.{/b}"

    j "20 units sounds plenty! I heard that the workload at UCI is heavy too because
    we are the best university in the area."

    MC "I heard the same thing. I think I’ll start with 12 units for the first
    quarter and see how that goes."

    j "Sounds reasonable."

    "{i}You each continue looking for information.{/i}"

    j "Hey look what I found here! {b}If you take any AP classes or classes from
    another college, you have to explicitly request prerequisites clearance for
    every course that requires those.{/b}"

    viv "I’ll try to remember that, I took some AP classes last year."

    MC "Me too."

    j "I found something else that's important. {b}Cheating is absolutely not tolerated.{/b}"

    show vivian_right_poker at right

    viv "Er...Is it tolerated anywhere?"

    MC "Maybe they think it's tolerated everywhere except here..."

    j "Yeah, maybe that’s what they think..."

    hide vivian_right_poker
    show vivian_right_default at right

    viv "Anyway, let’s see what else we can find."

    "{i}You each continue looking for information, more thoroughly this time.{/i}"

    MC "I found something interesting. We can easily keep track of our progress
    towards a degree by assessing DegreeWorks, which should be available by the
    winter quarter of our first year."

    viv "Nice! I’m glad they provide something like that."

    j "Yeah, it’ll make it a lot easier for us!"

    "{i}Suddenly, Peter The Anteater appears out of what one could call it, 'thin air'{/i}"

    show peter_right_evil at right

    hide vivian_right_default
    show jason_left_poker at left
    show vivian_left_fear behind jason_left_poker

    viv "Eeeeeppp"

    j "Yeah, yeah. Let's just get it over with."

    p "IT'S QUIZ TIME!"

    hide jason_left_poker
    hide jason_left_default
    hide vivian_left_fear
    hide vivian_right_poker

    # start of quiz 2

    label q2q1:

        $ q2result = 0

        menu:

            #question 1
            "When is the deadline to drop without a 'W' on your transcript?"

            "By the end of the second week of instruction":
                $ q2result += 1
                jump q2q2

            "After the first day of instruction":
                jump q2q2

            "Before the first day of instruction":
                jump q2q2

            "Before the fifth week of instruction":
                jump q2q2

    label q2q2:

        menu:

            #question 2
            "How many units are you allowed to take in a quarter?"

            "16. Any more classes need to be discussed with academic advisors.":
                jump q2q3

            "24. Any more classes need to be discussed with academic advisors.":
                jump q2q3

            "18. Any more classes need to be discussed with academic advisors.":
                jump q2q3

            "20. Any more classes need to be discussed with academic advisors.":
                $ q2result += 1
                jump q2q3

    label q2q3:

        menu:

            #question 3
            "If you took AP classes or classes from another college, you should?"

            "Take the  class again at UCI":
                jump q2q4

            "Let the UCI advisors know about it":
                jump q2q4

            "Request prerequisite clearance for the first class that needs those prerequisites":
                jump q2q4

            "Request prerequisite clearance for every class that needs those as prerequisites":
                $ q2result += 1
                jump q2q4

    label q2q4:

        menu:

            #question 4
            "Cheating at UCI is:"

            "Semi-tolerated":
                jump q2q5

            "Resolved on a case-by-case basis":
                jump q2q5

            "200%% tolerated":
                jump q2q5

            "Absolutely not tolerated":
                $ q2result += 1
                jump q2q5

    label q2q5:

        menu:

            #question 5
            "Where can you see your progress towards your major and minors and get all your academic status?"

            "Viewing your unofficial transcript ":
                jump q2result

            "Study list on the website ":
                jump q2result

            "DegreeWorks ":
                $ q2result += 1
                jump q2result

            "WebReg":
                jump q2result

    label q2result:

        p "The result of your quiz is..."

        p "%(q2result)s out of 5. Which means..."

        if q2result >= 4:

            show peter_right_happy at right

            p "YOU PASSED!"

        else:

            p "You failed."

            p "As per UCI policy, I will forget your current score if you receive a
            passing score for this retake quiz."

            p "Which starts now!"

            jump q2q1

        hide peter_right_happy
        show peter_right_evil at right

        p "You were successful this time, but will you be for the future quizzes?"

        p "See you real soon!"

        hide peter_right_evil

    show vivian_right_excited at right
    show jason_left_default at left

    viv "I'm so glad that's over!"

    j "Let's get out of here."

    hide vivian_right_excited
    hide jason_left_default

    "{i}You all walk out of the Aldrich Hall building together{/i}"

    scene ring_road
    with fade

    show vivian_right_default at right
    show jason_left_default at left

    "{i}As you all walk down Ring Road, two parallel monoliths appear between the trees{/i}"

    "{i}Jason points towards the buildings{/i}"

    j "Hey, what are those for?"

    viv "Let's go check it out!"

    scene gateway
    with fade

    show vivian_right_default at right
    show jason_left_default at left

    MC "We don’t have that much time though. Let’s split up and find out what we can,
     then we can all meet up again to share our info."

    j "Sounds like a good idea! I’ll go with Vivian to the building on the right...The Gateway Study Center."

    j "[name], can you go check out Langson Library?"

    MC "Sure, sounds good! Let’s meet back here in 10 minutes!"

    hide vivian_right_default
    hide jason_left_default

    scene langson
    with fade

    "{i}You walk into Langson Library through the motion sensor activated doors and
    quickly spy a wooden table to my right.{/i}"

    "{i}On top of it lies 2 stacks of flyers stating: 'Available Resources'. The
    one on the left is titled 'Langson' on the top and the other is titled 'Science Library'.{/i}"

    "{i}You start reading the Langson flyer{/i}"

    "{b}{i}For more information:{/b}{/i} {a=https://www.lib.uci.edu/langson}https://www.lib.uci.edu/langson{/a}"

    "{i}You continue to read what's listed immediately underneath it{/i}"

    "{b}{i}Take this virtual tour!{/b}{/i} {a=https://www.lib.uci.edu/langson/langson-floor-1}https://www.lib.uci.edu/langson/langson-floor-1{/a}"

    MC "How interesting!"

    "{i}You start to wonder what is in the Science Library.{/i}"

    "{i}You keep reading to find another section.{/i}"

    "{b}{i}Take this Science Library tour!{/b}{/i}  {a=https://www.lib.uci.edu/science-library/science-floor-1}https://www.lib.uci.edu/science-library/science-floor-1{/a}"

    "{i}Having learned everything about the UCI libraries, you begin to leave...{/i}"

    "{i}But suddenly...{/i}"

    "{i}Peter The Anteater appears!{/i}"

    show peter_left_default

    p "It seems that I got you alone this time."

    p "Regardless..."

    show peter_left_evil

    p "YOU SHALL NOT PASS until you take the Gateway Study Center tour."

    "{i}Unable to leave, you begin to take the tour...{/i} {a=https://www.lib.uci.edu/gateway-study-center/floor-2}https://www.lib.uci.edu/gateway-study-center/floor-2{/a}"

    p "Not so fast! Because it's QUIZ TIME!"

    # start of Quiz 3
    label q3q1:

        $ q3result = 0

        menu:

            #question 1
            "How much does printing cost?"

            "$0.10 per page":
                jump q3q2

            "$0.15 per page":
                jump q3q2

            "$0.12 per page":
                $ q3result += 1
                jump q3q2

            "Free for UCI students":
                jump q3q2


    label q3q2:

        menu:

            #question 2
            "Which floor are new books/magazines first released in Langson Library?"

            "2nd floor":
                $ q3result += 1
                jump q3q3

            "4th floor":
                jump q3q3

            "3rd floor":
                jump q3q3

            "1st floor":
                jump q3q3


        label q3q3:

            menu:

                #question 3
                "Which building is the Writing Center located in?"

                "Science Library":
                    $ q3result += 1
                    jump q3q4

                "Langson Library":
                    jump q3q4

                "The Gateway Study Center":
                    jump q3q4

                "Bren Events Center":
                    jump q3q4


        label q3q4:

            menu:

                #question 4
                "Which building are the multimedia resources located in?"

                "Langson Library":
                    jump q3q5

                "The Gateway Study Center":
                    jump q3q5

                "Bren Events Center":
                    jump q3q5

                "Science Library":
                    $ q3result += 1
                    jump q3q5


        label q3q5:

            menu:

                #question 5
                "Is the Gateway Study Center a “quiet study area”?"

                "No":
                    jump q3q6

                "Only on the weekends":
                    jump q3q6

                "Only after 5PM":
                    jump q3q6

                "Yes":
                    $ q3result += 1
                    jump q3q6

        label q3q6:

            menu:

                #question 6
                "How do we get our own space in the library?"

                "First come first serve policy":
                    jump q3result

                "Book them through: www.lib.uci.edu/study-space-locator":
                    $ q3result += 1
                    jump q3result

                "2 hour max usage policy":
                    jump q3result

                "Ask the librarian":
                    jump q3result

        label q3result:

            p "The result of your quiz is..."

            p "%(q3result)s out of 6. Which means..."

            if q3result >= 5:

                show peter_left_happy

                p "YOU PASSED!"

            else:

                p "You failed."

                p "As per UCI policy, I will forget your current score if you receive a
                passing score for this retake quiz."

                p "Which starts now!"

                jump q3q1

            hide peter_left_happy
            show peter_left_evil

            p "You were successful this time, but will you be for the future quizzes?"

            p "See you real soon!"

            hide peter_left_evil

    hide peter_left_default
    "{i} You walk out of the library{/i}"

    scene gateway
    with fade

    show vivian_left_poker at left
    show jason_right_poker at right

    "{i}As soon as you walk out, you see Vivian and Jason leaving the opposite building.
    Vivian spots you first.{/i}"

    viv "Hey [name]! Did you get stopped and quizzed too?"
    MC "Yeah, I had to learn everything about all the study resources."
    j "Oh darn. Bummer that we couldn’t spread the work, but hey, at least we all know about the school’s study resources now!"
    hide jason_right_poker
    hide vivian_left_poker
    "{i} The group leaves the twin study centers together and walk back towards ring road. {/i}"

    scene ring_road
    with fade

    MC "I am getting a bit tired of all this though..."
    show jason_right_fear at right
    j "Yeah...all this walking is making me really tired..."
    show vivian_left_poker at left
    viv "I think [name] meant the quizzing Jason."
    hide jason_right_fear
    show jason_right_poker at right
    j "..."
    MC "..."
    viv "..."

    scene bus
    with fade

    "{i} They walk towards a pair of flagpoles and see several busses with UCI logos waiting there.{/i}"
    MC "Anyways... Let's go check out those busses and see where they'll take us!"
    hide vivian_left_poker
    show vivian_left_happy at left
    viv "Good idea! Let's go!"
    hide vivian_left_happy
    hide jason_right_poker

    "{i} The trio board the Peter driven bus which rolls down Campus and turns down California before arriving at a building. {/i}"

    scene ARC_outside
    with fade

    show peter_left_default
    p "Welcome to the Anteater Recreational Center (ARC). Here you'll find all sorts of fun, physical activites! Please watch your feet as you exit the bus."
    hide peter_left_default
    "{i} We leave the bus and enter the ARC. {/i}"

    #Start building #4
    show jason_left_excited at left
    j "Come on let’s check it out!"
    #(a different visual from inside the ARC)
    "{i} We enter the building. {/i}"

    scene ARC_inside1
    with fade

    MC "Woah! Look at that gym and the indoor courts! They're massive!"
    show vivian_right_excited at right
    show jason_left_excited at left
    viv "Hey check this out!"

    "{i}Vivian gestures to the entry hand scanner system{/i}"

    viv "What a neat entry system! It says here that all freshmen have to sign up here before entering the ARC. You’re supposed to punch in your UCI student ID and then scan your hand for entry. This is pretty cool!"
    MC "It also says that we can get our friends in too by getting an ARC day pass."
    j "Really?! I’ll be bringing my friends over to play ball with me all the time!"
    MC "Yeah! Let’s go check out what other activities and sports we can play in here."

    scene ARC_inside2
    with fade

    show vivian_right_excited at right
    show jason_left_excited at left

    viv "Look! There's a swimming pool out back! Let's all go for a dip someday!"
    j "I'm not much of a swimmer but I'm down! Did you see the racquetball courts though? Those glass walls look so amazing. You can even turn them into volleyball courts!"
    MC "They have so many activities we could spend all day here. Let's take a look at the ARC’s {a=https://www.campusrec.uci.edu/arc/facilities.asp}facilities map{/a}."
    j "Hmmm... Let me see... The ARC offers all these sports, both indoor and outdoor. On top of that, there is a club for nearly every sport!."
    viv "Oh! They also offer a variety of different classes to learn. They have martial arts, rock climbing, rowing, dance, and even cooking classes! That’s amazing!"
    j "Where'd you see those Vivian?"
    viv "Here in this {a=https://www.campusrec.uci.edu/classes/index.asp}pamphlet{/a}!"
    MC "Hmmm... Rowing sounds like something I would definitely like to learn. Their club even goes to Newport beach for practice."
    j "I found a hiking club too; the group goes on hikes every other weekend. That’s more up my alley."
    viv "If I have a baseball club and want to invite other teams from other universities, I can fill an application and book the field. That’s pretty convenient! This is the {a=https://www.campusrec.uci.edu/arc/includes/Facility-Reservation-Application.pdf}form{/a}."
    MC "How soon do I have to make a reservation/rental inquiry?"
    viv "Reservations can be made up to a quarter in advance for most activities. All requests must be submitted at least two weeks from the date of the desired event in order to receive consideration."
    j "This is all pretty interesting but a lot. Let's get some fresh air and check out the outdoor fields."
    #( a few pictures of the outdoor basketball, soccer and tennis courts)
    viv "That was a lot of exploration. The ARC really offers a lot of activities! I'd love to just spend my entire day here but we have to get going."
    hide vivian_right_excited
    hide jason_left_excited
    show vivian_right_fear at right
    show peter_left_evil at left
    p "Leaving so soon? What’s the rush Vivian?"
    viv "I guess we completely forgot about the quiz."
    p "That's RIGHT! Now answer these questions..."

    hide vivian_right_fear

    # start of Quiz 4
    label q4q1:

        $ q4result = 0

        menu:

            #question 1
            "How do you enter the ARC?"

            "Just go in swipe your ID card":
                jump q4q2

            "Punch in your number and get your hand scanned":
                $ q4result += 1
                jump q4q2

            "Just say “hi” at the front desk and you can enter":
                jump q4q2

            "Just type in your student ID at the entry gate":
                jump q4q2


    label q4q2:

        menu:

            #question 2
            "Can you bring a non-UCI person to the ARC and how?"

            "Yes. By getting a day pass for them":
                $ q4result += 1
                jump q4q3

            "Yes. By signing them up and getting their hand scanned":
                jump q4q3

            "No. UCI is very strict about it’s only UCI student policy":
                jump q4q3

            "No. But you can surely sneak them in":
                jump q4q3


    label q4q3:

        menu:

            #question 3
            "Which class does the ARC not offer?"

            "Martial Arts":
                jump q4q4

            "Cooking":
                jump q4q4

            "Tennis":
                jump q4q4

            "Skydiving":
                $ q4result += 1
                jump q4q4


    label q4q4:

        menu:

            #question 4
            "What is the facility application reservation form for?"

            "To reserve a spot in a club in the ARC":
                jump q4q5

            "To make a reservation for a new sports club in UCI":
                jump q4q5

            "To reserve a court/field/room etc. for events for your club":
                $ q4result += 1
                jump q4q5

            "To reserve rooms to hold private parties":
                jump q4q5


    label q4q5:

        menu:

            #question 5
            "How soon does one have to submit the facility application reservation?"

            "A quarter before the event is scheduled":
                jump q4result

            "48hrs before the event is scheduled":
                jump q4result

            "2 weeks before the event is scheduled":
                $ q4result += 1
                jump q4result

            "At least a month before the event is scheduled":
                jump q4result

    label q4result:

        p "The result of your quiz is..."

        p "%(q4result)s out of 5. Which means..."

        if q4result >= 4:
            hide peter_right_evil
            show peter_left_happy at left

            p "YOU PASSED!"

        else:

            p "You failed."

            p "As per UCI policy, I will forget your current score if you receive a
            passing score for this retake quiz."

            p "Which starts now!"

            jump q4q1

        p "Congratulations! You passed all the quizzes. Welcome to UCI!"

        "{i}You can't help but feel a wave of accomplishment, but also a little sadness{/i}"

        MC "So what happens to you now?"

        p "I am going back to welcome the next wave of students. This is part of
        the new, never before seen orientation package for the 2021-2022 academic year."

        show vivian_right_poker at right

        viv "Wait...you mean we tried so hard to pass those quizzes but that was all part of the plan?"

        p "Bye now!"

        hide peter_left_happy
        hide _peter_left_evil

        "{i}Zot... Zot.. Zot.{/i}"

        show jason_left_excited at left
        show vivian_right_excited at right

        MC "I can’t believe we made it. We passed all the quizzes!"

        j "Yeah, that was challenging to say the least."

        viv "I think we’ll remember all of this important information for a long time."

        j "For sure! I've never done anything like this before."

        MC "I think UCI is really good at getting our attention."

        show jason_left_poker at left

        j "Yeah. Well, all that effort for nothing."

        viv "Maybe the real reward is the UCI experience."

        hide jason_left_poker

        MC "Maybe the real reward is the friendship we make along the way."

        j "Maybe the friendship is part of the UCI experience too!"

        viv "You’re right. I’m so happy that I chose to attend UCI.
        I’m sure I made the right choice!"

        MC "Me too. UCI is the best school ever!"

    # This ends the game.

    return
