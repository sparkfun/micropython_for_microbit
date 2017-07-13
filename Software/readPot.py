# Experiment 1.1
# Reading a Potentiometer

from microbit import *

while True:
    potentiometerVal = pin2.read_analog()
    pin0.write_analog(potentiometerVal)
    sleep(25)
