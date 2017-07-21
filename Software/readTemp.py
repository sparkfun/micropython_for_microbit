# SparkFun Electronics
# Experiment 7.0
# Reading a Temp Sensor

from microbit import *

while True:
    rawTemp = pin2.read_analog()
    degC = (((rawTemp*3.3)/(1023))-0.5)*100
    display.show(str(degC))
    sleep(1000)
