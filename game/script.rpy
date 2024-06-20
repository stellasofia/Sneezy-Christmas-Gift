define e = Character("Sneezy")
define z = Character("Klaus")
default location = "bg scene1"

# Variable, die dazu dient, temporär Information über das aktuell aufgesammelte Item zu speichern
default item_picked_up = "N/A"

# Einfache boolean-Lösung als Indikator ob man das entsprechende Item besitzt
default paper = False
default ribbon = False
default gloves = False
default driedgloves = False
default present = False
default sneezy_talkcounter = 0
# neu
default klaus = False
default sleight = False
default cookie = False
default presentCheck = False #FALSE
default klaus_talkcounter = 0 #0
default sleightChecked = False
default dough = False
default cookierolled = False
default puzzlecomplete = False

image snow1 = Fixed(SnowBlossom("/images/animated/snow/snow1.png", 50, xspeed=(20, 50), yspeed=(100, 200), start=50))
image snow2 = Fixed(SnowBlossom("/images/animated/snow/snow2.png", 50, xspeed=(20, 50), yspeed=(100, 200), start=50))


init python:

    myfade = Fade(0.3, 0.2, 0.3)

    def change_scene_with_slow_fade(new_location):
        global location
        location = new_location
        renpy.scene(location)
        renpy.with_statement(Fade(1.0, 0.2, 1.0))



label start:
    show snow1
    show snow2
    # Erste Szene nach dem Start eines neuen Spiels
    narrator "This game is currently in development, this is not the final version of this game."

    play music "audio/music/Music2.mp3" fadein 1.0 volume 0.2

    # Nach der ersten Szene wird der Spieler direkt in den Gameplay Loop gesetzt
    jump loop

    return

# Das Label sorgt dafür, dass das Gameplay bis zu einem bestimmten Punkt immer wieder geloopt wird, in dem jedes andere Label wieder zum Loop springt, wenn alles andere erledigt wurde
label loop:

    # Ändert den Hintergrund zu der aktuellen Location (in Variable location gespeichert)
    scene expression location

    # Ruft die Screen-Funktion der Location auf
    call screen locationScreen

    return

# Das Label dient zur Aufsammlung des Items, welches im Screen vorher definiert wird
label collecting:
    if item_picked_up == "ribbon":
        play sound "audio/fx/backpack1.mp3" volume 0.5
        narrator "I've found a beautiful ribbon! Maybe I can use it for someting later."
        # Variablen in Labels zu verändern, wird nur durch $ vor dem Variablennamen zugelassen.
        $ ribbon = True
    elif item_picked_up == "gloves":
        play sound "audio/fx/backpack2.mp3" volume 0.5
        narrator "Look what we have here! Gloves buried in the snow, though they seem thoroughly soaked."
        $ gloves = True
    elif item_picked_up == "paper":
        play sound "audio/fx/paper1.mp3" volume 0.5
        narrator "Wonderful! I've got my hands on some wrapping paper - just what I needed!"
        $ paper = True
    elif item_picked_up == "dough":
        $ dough = True
        narrator "Got my hands on some dough!"


    # Nach dem Check wird die item_picked_up Variable zur Prävention vor Bugs zurückgesetzt und der Spieler wieder zurück in den Loop geworfen, um ihn wieder die Kontrolle zu geben.
    $ item_picked_up = "N/A"
    jump loop

    return

# Label, welches aufgerufen wird, wenn man den Table in Scene 3 anklickt
label table:
    if present == True:
        narrator "the workbench"
        jump loop
    # Überprüfung ob alle Items gesammelt wurden
    if ribbon == True and paper == True and gloves == True and driedgloves == True:
        play sound "audio/fx/workbench1.mp3" volume 0.5
        narrator "Carefully assembling all the items, you've successfully crafted a beautifully wrapped present!"
        $ present = True
        jump loop
    else:
        play sound "audio/fx/success1.mp3" volume 0.5
        narrator "Oh, look! Maybe if I've found more items I could use the workbench to craft a present."
        jump loop


label sneezydialogue:
    if present == True and sneezy_talkcounter >= 3 and presentCheck == False:
        menu:
            "Do you want to give the present to Sneezy?"
            "Hand over the gift":
                e "That's incredibly thoughtful of you."
                narrator "As you hand over the gift, Sneezy's eyes sparkle with joy."
                narrator "He gently unwraps the present, the paper slightly dampened by his snowy touch, but it reveals a pair of snug, warm gloves."
                narrator "Overflowing with gratitude, Sneezy wraps you in a cozy snowman hug, radiating warmth despite his chilly exterior."
                narrator "The snowfall seems to twinkle with joy as you've truly made Sneezy's Christmas special."
                $ presentCheck = True

                jump loop
            "Don't":
                narrator "You decide to keep the gift for now, maybe for another time."
                jump loop
    if presentCheck == True:
        e "Now with these gloves there is nothing holding me back."
        e "Have you met Klaus yet? I've heard he needs some help as well!"
        jump loop
    

    if presentCheck == False or present == False:
        if sneezy_talkcounter == 0:
            e "Well, hello there, my new friend! It's a delight to make your acquaintance. I'm Sneezy!"
            menu:
                "Hey there!":
                    narrator "Hey there! What's the snow report today?"
                    e "The snow's as fluffy as ever! Just the way I like it."
                "Hi Sneezy. Nice to meet you":
                    narrator "Hi, Sneezy. It's a pleasure to meet someone as unique as you!"
            $ sneezy_talkcounter = 1
            jump loop
        elif sneezy_talkcounter == 1:
            e "Well, you see, I'm trying to wrap Christmas presents for everyone, but there's a little issue."
            e "Being made of snow makes the wrapping paper wet, and it keeps tearing. It's so frustrating!"
            $ sneezy_talkcounter = 2
            jump loop
        elif sneezy_talkcounter == 2:
            e "I'm feeling confident this time!"
            e "Oh no... wet again."
            e "Third time's the charm, right?"
            $ sneezy_talkcounter = 3
            jump loop
        elif sneezy_talkcounter == 3:
            e "Would you like to learn how to wrap presents?"
            e "What would you start with?"
            menu:
                "Finding the perfect gift":
                    e "Absolutely! Everyone has unique preferences. It's essential to consider what the other person would truly appreciate."
                    e "The most important thing is that it comes from the heart."
                "Selecting the right wrapping materials":
                    e "That's correct."
                    e "I enjoy adding a ribbon to the presents I wrap, although I usually don't get that far."
                    e "But let's say I really like the idea of it."
            $ sneezy_talkcounter = 4
            jump loop
        elif sneezy_talkcounter == 4:
            e "Do you want to continue and learn more about the art of gift wrapping?"
            menu:
                "Tell me about the necessary tools":
                    narrator "What tools do I need to get started?"
                    e "There are four essential things to consider:"
                    e "1. Choosing the perfect gift."
                    e "2. Selecting the right wrapping materials."
                    e "3. Ensuring it's neatly wrapped and sealed."
                    e "4. Having a suitable workspace for crafting the gift."
                "I think I've got it":
                    e "Alrighty then! Feel free to ask if you ever need more advice."
            jump loop
        jump loop
    jump loop


label narratordialog:
    if gloves == False:
        narrator "This place offers the perfect warmth to counter the cold outside."
        jump loop
    elif gloves == True and driedgloves == False:
        menu:
            "What will you do with your gloves?"
            "Dry gloves":
                $ driedgloves = True
                narrator "You decide to dry your gloves by the warmth of the fireplace."
                narrator "They now are as good as new."
                jump loop
            "Leave":
                narrator "You choose to leave your gloves as they are."
                jump loop
    elif gloves == True and driedgloves == True and presentCheck == False:
        narrator "Really warm and cozy."
        jump loop


label oven:
    if dough == False or cookie == True:
        narrator "Nice and warm."
        jump loop
    if dough == True and cookie == False:
            menu:
                "Would you like to bake the dough?"
                "Yes, let's bake it!":
                    $ cookie = True
                    narrator "As the cookie bakes, a warm, enticing aroma fills the room, evoking memories of home and comfort."
                    jump loop
                "No, not yet.":
                    narrator "Deciding against baking for now, you take a moment to ponder your next move."
                    jump loop
    jump loop




label klausdialog:
    if klaus_talkcounter == 0:
        if presentCheck == True:
            z "Oh hey there!"
            z "I've been zipping around, delivering gifts to all the townsfolk."
            z "However, my landing was a tad... rough, shall we say."
            z "Now, my sleigh's acting up a bit."
            $ klaus_talkcounter = 1
            jump loop
        elif presentCheck == False:
            z "hmm...."
            z "How can I fix it..."
            narrator "seems like he is lost in thought"
            jump loop
    elif klaus_talkcounter == 1:
        z "Ah, my name is Klaus by the way."
        $ klaus_talkcounter = 2
        jump loop
    elif klaus_talkcounter == 2 and sleightChecked == False:
        z "could you take a look on how the sleight is looking?"
        jump loop
    elif klaus_talkcounter == 2 and sleightChecked == True:
        z "Ah, I see."
        z "You mentioned a piece is missing?"
        z "Any thoughts on how we might fix it?"
        menu:
                "Replace the entire sleigh":
                    z "Wow, that's certainly one way to go about it, though perhaps not the most practical."
                    z "But, you've sparked an idea in me!"
                "Replace the missing piece":
                    z "That's a solid suggestion."
        z "You see, the sleigh is crafted from gingerbread."
        z "Unfortunately, I'm quite the terrible baker."
        $ klaus_talkcounter = 3
        jump loop
    elif puzzlecomplete == True:
        z "Wow, buddy, you're the best!"
        z "Hope to cross paths again sometime."
        z "I must be off now, those presents won't deliver themselves."
        z "Take care, and Merry Christmas, my friend."
        scene black
        narrator "The End."
        return
    elif klaus_talkcounter == 3 and cookie == True:
        z "Oh, you found the missing piece, eh?"
        z "Let's try putting it all back together."
        jump loop
    elif klaus_talkcounter == 3:
        z "Let's head into the hut and bake to our heart's content."
        z "Well, to your heart's content."
        z "I'll be right here, eagerly awaiting."
        jump loop
    
    

label sleightAction:
    if cookie == True and klaus_talkcounter >= 3 and puzzlecomplete == False:
        narrator "start minigame"
        $ sleightChecked = True
        $ puzzlecomplete = True
        $setup_puzzle()
        call screen reassemble_puzzle
        #
        # TO END GAME
        #
        #scene black
        #narrator "The End."
        #return
        jump loop
    elif puzzlecomplete == True:
        narrator "Seems to be fixed!"
        jump loop
    else:
        narrator "Seems like a piece is missing"
        $ sleightChecked = True
        jump loop


    jump loop
    return
