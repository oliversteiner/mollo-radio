from radio import radio, cli, gpio
from gpiozero import Button
from signal import pause

ip = "10.0.1.99"
port = 6612
radio = radio.Radio(ip, port)

if __name__ == "__main__":
    try:
       # cli.main(radio)
        gpio.main(radio)
    except KeyboardInterrupt:
        pass

