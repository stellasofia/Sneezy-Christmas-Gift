default page_pieces = 4
default full_page_size = (365, 338)
default piece_coordinates = [(878, 478), (1060, 478), (878, 646), (1060, 646)]
default initial_piece_coordinates = []
default finished_pieces = 0
define dissolve = Dissolve(0.5)


init python:
    def setup_puzzle():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)

    def piece_drop(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1
            play_sound("audio/fx/hammer1.mp3", 0.1)

        if finished_pieces == page_pieces:
            renpy.jump("loop")

screen reassemble_puzzle:
    image "/minigame1/background.png"
    add "snow1"
    add "snow2"
    add "snow3"
    frame:
        background "/minigame1/puzzle-frame.png"
        xysize full_page_size
        anchor(0.5, 0.5)
        pos(975, 565)

    draggroup:
        for i in range(page_pieces):
            drag:
                drag_name i
                pos initial_piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                drag_raise True
                image "/minigame1/Pieces/piece-%s.png" % (i + 1)

        #snap spots
        for i in range(page_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                image "/minigame1/Pieces/piece-%s.png" % (i + 1) alpha 0.0 #unsichtbar

                
