# OLED: I2C
# PIN 03 - SDA GPIO 2
# PIN 05 - SCL GPIO 3
# PIN 02 - 5V
# PIN 06 - GND

# Display: ssd1306
# Interface: i2c
# Dimensions: 128 x 64
# Yellow:   0 - 12 ?
# Blue:     13 - 50 ?

# https://luma-oled.readthedocs.io/en/latest/hardware.html
#
# sudo usermod -a -G spi,gpio,i2c USER
#

from PIL import ImageFont
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from pathlib import Path

serial = i2c(port=1, address=0x3C)
font_path = str(Path(__file__).resolve().parent) + "/fonts/"


def make_font(name, size):
    font = font_path + name
    return ImageFont.truetype(font, size)


def vol_plank(vol):
    num = 128 / 100 * vol
    return num


def show(text, vol):
    device = ssd1306(serial)

 #   while True:
    font = make_font("FreePixel.ttf", 40)

    # with canvas(device) as draw:
    #     draw.rectangle(device.bounding_box, outline="white", fill="black")
    #     draw.text((1, 14), text, fill="white", size=20)
    #

    with canvas(device) as draw:
        # links, oben, länge, höhe
        left = 5
        top = 0
        length = vol_plank(vol)
        height = 2
        draw.rectangle([left, top, length, height], fill="white")
        draw.text((10, 15), text=text, font=font, fill="white")



if __name__ == "__main__":
    try:
        show("DRS 1", 50)
    except KeyboardInterrupt:
        pass
