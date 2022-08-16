from gpiozero import  RotaryEncoder
from signal import pause

# Rotary Encoder:
rotor = RotaryEncoder(6, 13, wrap=True, max_steps=150)
rotor.steps = 1


def change_volume():
    print(rotor.steps)


rotor.when_rotated = change_volume

# Keep Script going
pause()
