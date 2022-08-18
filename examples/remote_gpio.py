# Run with:
# $ GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=10.0.1.99 python3 remote_gpio.py

from gpiozero import Button
# from gpiozero import RotaryEncoder

from signal import pause

last_button = 0


def change_button(num):
    global last_button
    last_button = num
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


def play_song_3():
    if last_button == 3:
        print("same")
    else:
        print("Button 3 pressed")
    change_button(3)


def change_volume():
    print('rotate')
  #  print(rotor.steps)


# Rotary Encoder:
#rotor = RotaryEncoder(6, 13, wrap=True, max_steps=150)
#rotor.steps = 10

button1 = Button(23)  # DRS 1
button2 = Button(16)  # MW
button3 = Button(5)  # Play / Pause

print('remote test 2')
print('---------------')

#rotor.when_rotated = change_volume
button1.when_pressed = play_song_1
button2.when_pressed = play_song_2
button3.when_pressed = play_song_3

pause()
