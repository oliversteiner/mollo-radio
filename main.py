from radio import radio, cli
from gpiozero import Button
from signal import pause

ip = "10.0.1.99"
port = 6610
radio = radio.Radio(ip, port)

if __name__ == "__main__":
    try:
        cli.main(radio)
    except KeyboardInterrupt:
        pass

    button1 = Button(23)  # DRS 1
    button2 = Button(16)  # MW
    button3 = Button(5)  # Play / Pause

    button1.when_pressed = radio.play_song(1)
    button2.when_pressed = radio.play_song(2)
    button3.when_pressed = radio.play_pause()

    pause()
