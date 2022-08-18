# OLED: I2C
# PIN 03 - SDA GPIO 2
# PIN 05 - SCL GPIO 3
# PIN 02 - 5V
# PIN 06 - GND

# https://luma-oled.readthedocs.io/en/latest/hardware.html
#
# sudo usermod -a -G spi,gpio,i2c USER
#

import time
import datetime
# from demo_opts import get_device
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

serial = i2c(port=1, address=0x3C)


def main(text):
    # device = get_device()
    device = ssd1306(serial)
    while True:
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((10, 10), text, fill="white")
            device.show()


if __name__ == "__main__":
    try:
        main("Hello World")
    except KeyboardInterrupt:
        pass
