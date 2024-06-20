# Screen-Funktion für jegliche Interaktion
screen locationScreen():
    # Überprüft die aktuelle Location, um die richtigen Interaktionen & Bilder zu zeigen


    if location == "bg scene1":
        add "snow1"
        add "snow2"

        #Star-Button zu Scene2
        imagebutton:
            idle "animated_star"
            hover "/animated/star/animated_star_hover.png"
            xpos 700
            ypos 300
            action [
                Function(lambda: play_sound("audio/fx/snow_walk1.mp3", 0.5)),
                SetVariable("location", "bg scene2"),
                With(Fade(1.0, 0.2, 0.5)),
                Jump("loop")
            ]
        imagebutton:
            idle "animated_star"
            hover "/animated/star/animated_star_hover.png"
            xpos 500
            ypos 500
            action [
                Function(lambda: play_sound("audio/fx/snow_walk1.mp3", 0.5)),
                SetVariable("location", "bg scene4"),
                With(Fade(1.0, 0.2, 0.5)),
                Jump("loop")
            ]

        # Überprüft ob man das Item schon aufgesammelt hat
        if ribbon == False:
            imagebutton:
                idle "ribbon.png"
                hover "ribbon_hover.png"
                xpos 300
                ypos 700
                action [SetVariable("item_picked_up", "ribbon"), Jump("collecting")]

        if gloves == False:
            imagebutton:
                idle "gloves.png"
                hover "gloves_hover.png"
                xpos 1400
                ypos 580
                action [SetVariable("item_picked_up", "gloves"), Jump("collecting")]

    elif location == "bg scene2":
        add "snow1"
        add "snow2"

        #Star-Button zu Scene3
        imagebutton:
            idle "animated_star"
            hover "/animated/star/animated_star_hover.png"
            xpos 950
            ypos 660
            action [
                Function(lambda: play_sound("audio/fx/door1.mp3", 0.5)),
                Function(lambda: play_channel("audio/fx/fire1.mp3", "fire_channel", 0.5, 0.5)),
                SetVariable("location", "bg scene3"),
                With(Fade(0.5, 0.2, 0.5)),
                Jump("loop")
            ]
        imagebutton:
        #Star-Button zu Scene1
            idle "animated_star"
            hover "/animated/star/animated_star_hover.png"
            xpos 1200
            ypos 910
            action [
                Function(lambda: play_sound("audio/fx/snow_walk1.mp3", 0.5)),
                SetVariable("location", "bg scene1"),
                With(Fade(1.0, 0.2, 0.5)),
                Jump("loop")
            ]
        imagebutton:
        #Sneezy-Button
            idle "animated_speech_bubble"
            hover "/animated/speech_bubble/animated_speech_bubble_hover.png"
            xpos 620
            ypos 450
            action [Jump("sneezydialogue")]

        if presentCheck == True:
            imagebutton:
                idle "r_glove.png"
                xpos 650
                ypos 540
            imagebutton:
                idle "l_glove.png"
                xpos 260
                ypos 520




    if location == "bg scene3":
        #Star-Button zu Scene2
        imagebutton:
            idle "animated_star"
            hover "/animated/star/animated_star_hover.png"
            xpos 920
            ypos 910
            action [
                Function(lambda: play_sound("audio/fx/door2.mp3", 0.5)),
                Function(lambda: stop_channel("fire_channel", 0.5)),
                SetVariable("location", "bg scene2"),
                With(Fade(0.5, 0.2, 0.5)),
                Jump("loop")
            ]
        imagebutton:
            idle "table.png"
            hover "table_hover"
            xpos 1250
            ypos 550
            action Jump("table")

        imagebutton:
        #Fireplace
            idle "fireplace.png"
            hover "fireplace_hover.png"
            xpos 380
            ypos 550
            action Jump("narratordialog")


        if paper == False:
            imagebutton:
                idle "paper.png"
                hover "paper_hover.png"
                xpos 740
                ypos 450
                action [SetVariable("item_picked_up", "paper"), Jump("collecting")]

    if location == "bg scene4":
        add "snow1"
        add "snow2"

        imagebutton:
            idle "animated_star"
            hover "/animated/star/animated_star_hover.png"
            xpos 1050
            ypos 650
            action [
                Function(lambda: play_sound("audio/fx/door2.mp3", 0.5)),
                SetVariable("location", "bg scene5"),
                With(Fade(1.0, 0.2, 0.5)),
                Jump("loop")
            ]
        imagebutton:
            idle "animated_star"
            hover "/animated/star/animated_star_hover.png"
            xpos 750
            ypos 900
            action [
                Function(lambda: play_sound("audio/fx/snow_walk1.mp3", 0.5)),
                SetVariable("location", "bg scene1"),
                With(Fade(1.0, 0.2, 0.5)),
                Jump("loop")
            ]
        # CHANGE TO TRUE!
        if klaus == False:
            imagebutton:
                idle "animated_speech_bubble"
                hover "/animated/speech_bubble/animated_speech_bubble_hover.png"
                xpos 350
                ypos 460
                action Jump("klausdialog")

        # ALSO CHANGE TO TRUE!
        if sleight == False:
            imagebutton:
                    idle "sleight.png"
                    hover "sleight_hover.png"
                    xpos 1550
                    ypos 500
                    action Jump("sleightAction")


    if location == "bg scene5":
        imagebutton:
            idle "animated_star"
            hover "/animated/star/animated_star_hover.png"
            xpos 700
            ypos 900
            action [
                Function(lambda: play_sound("audio/fx/door2.mp3", 0.5)),
                SetVariable("location", "bg scene4"),
                With(Fade(1.0, 0.2, 0.5)),
                Jump("loop")
            ]
        imagebutton:
                    idle "fireplace.png"
                    hover "fireplace_hover"
                    xpos 760
                    ypos 540
                    action Jump("oven")

        if dough == False:
            imagebutton:
                        idle "dough.png"
                        hover "dough_hover.png"
                        xpos 1100
                        ypos 800
                        action [SetVariable("item_picked_up", "dough"), Jump("collecting")]

        #imagebutton:
                    #idle "rollingpin.png"
                    #hover "rollingpin_hover.png"
                    #xpos 1150
                    #ypos 600
