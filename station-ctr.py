from gpiozero import Button
from signal import pause


def button1_action():
    print("DRS 1!")


def button2_action():
    print("Mittelwelle")


def button1_action():
    print("Start Stop")


button1 = Button(23)  # DRS 1
button2 = Button(16)  # MW
button3 = Button(5)  # Start / Stop

button1.when_pressed = button1_action
button2.when_pressed = button2_action
button3.when_pressed = button1_action

pause()
