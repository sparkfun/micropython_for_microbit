# SparkFun Electronics
# Experiment 6.0
# Reading a button press

from microbit import *

led_pins = [pin0, pin1, pin2]
led_states = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
led_states_iter = iter(led_states)
RED = 0
GREEN = 1
BLUE = 2

while True:
    while pin16.read_digital() == 0:
        pass
    while pin16.read_digital() == 1:
        pass
    try:
        led_state = next(led_states_iter)
    except:
        led_states_iter = iter(led_states)
        
    pin0.write_analog(led_state[RED])
    pin1.write_analog(led_state[GREEN])
    pin2.write_analog(led_state[BLUE])
