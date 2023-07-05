# SparkFun Electronics
# Experiment 9.0
# Using a buzzer

from microbit import *
import music

# disable built-in speaker on micro:bit v2 and output to external speaker from pin P0
speaker.off()

while True:
    if pin15.read_digital() == 1:
        music.play("C4:8")
    elif pin16.read_digital() == 1:
        music.play("D1:8")
    else:
        pass
