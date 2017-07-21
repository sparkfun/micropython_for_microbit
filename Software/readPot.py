# SparkFun Electronics
# Experiment 2.0
# Reading a Potentiometer

from microbit import *

while True:
    potVal = pin2.read_analog()
    pin0.write_analog(potVal)
    sleep(25)
