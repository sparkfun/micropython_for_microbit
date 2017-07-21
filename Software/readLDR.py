# SparkFun Electronics
# Experiment 3.0
# Reading a Photoresistor

from microbit import *

calibrationVal = pin0.read_analog()
sleep(1000)

while True:
    lightVal = pin0.read_analog()
    if lightVal < calibrationVal-50:
        pin16.write_digital(1)
    else:
        pin16.write_digital(0)
