# SparkFun Electronics
# Experiment 4.0
# Driving an RGB LED

from microbit import *
from random import randint

redVal = randint(0, 255)
greenVal = 0
blueVal = 0

while True:
    if button_a.is_pressed():
        redVal = 0
        blueVal = 0
        greenVal = randint(0, 255)
        pin0.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin2.write_analog(blueVal)
    elif button_b.is_pressed():
        redVal = 0
        blueVal = randint(0, 255)
        greenVal = 0
        pin0.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin2.write_analog(blueVal)
    else:
        pin0.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin2.write_analog(blueVal)
