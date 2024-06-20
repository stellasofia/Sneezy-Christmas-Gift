init python:
    def play_sound(path, vol):
        renpy.sound.set_volume(vol)
        renpy.sound.play(path)

    renpy.music.register_channel("fire_channel", "sfx")

    def play_channel(path, chan, fade, vol):
        renpy.music.set_volume(vol, channel=chan)
        renpy.music.play(path, channel=chan, fadein=fade)

    def stop_channel(chan, fade):
        renpy.music.stop(channel=chan, fadeout=fade)
