# SparkFun Electronics
# Experiment 11
# Using the Compass (Magnetometer)

from microbit import *

compass.calibrate()
while True:
    bearing = compass.heading()
    sleep(10)

    #bearing is the degrees
    if ( bearing > 10 and bearing < 180 ):
        pin0.write_digital(0)
        pin16.write_digital(1)
    #bearing is the degrees
    elif ( bearing > 180 and bearing < 350 ):
        pin0.write_digital(1)
        pin16.write_digital(0)
    #bearing is the degrees
    else:
        pin0.write_digital(1)
        pin16.write_digital(1)
