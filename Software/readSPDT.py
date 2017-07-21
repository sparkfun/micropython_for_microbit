# SparkFun Electronics
# Experiment 5.0
# Reading an SPDT Switch

from microbit import *

while True:
    if pin0.read_digital():
        pin15.write_digital(1)
        sleep(1000)
        pin15.write_digital(0)
        sleep(1000)
    else:
        pin16.write_digital(1)
        sleep(500)
        pin16.write_digital(0)
        sleep(500)
