# Run with:

from gpiozero import Button
from gpiozero import RotaryEncoder

from signal import pause

# Rotary Encoder:
rotor = RotaryEncoder(6, 13, wrap=True, max_steps=100)
rotor.steps = 10
last_button = 0

button1 = Button(23)  # DRS 1
button2 = Button(16)  # MW
button3 = Button(5)  # Play / Pause
print("HW Controlls")


def main(radio1):
    print('gpio test 3')
    print('---------------')

    radio = radio1
    rotor.steps = radio.volume()

    def change_button(num):
        global last_button
        last_button = num
        radio.play_song(num)
        pass

    def play_song_1():
        print("!")
        if last_button == 1:
            print("same")
        else:
            print("Button 1 pressed")
            change_button(1)

    def play_song_2():
        if last_button == 2:
            print("same")
        else:
            print("Button 2 pressed")
            change_button(2)

    def pause_song():
        if last_button == 3:
            print("same")
        else:
            print("Button 3 pressed")
            radio.play_pause()

    def change_volume():
        print('rotate')
        print(rotor.steps)
        radio.set_volume(rotor.steps)

    rotor.when_rotated = change_volume
    button1.when_pressed = play_song_1
    button2.when_pressed = play_song_2
    button3.when_pressed = pause_song

    pause()
