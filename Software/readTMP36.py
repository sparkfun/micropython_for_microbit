# Experiment 1.6
# Reading the TMP36 Temperature Sensor

from microbit import *

while True:
    tmp36 = pin2.read_analog()
    cCalc = ((3.3/1023)*tmp36-.5)*100
    degC = round(cCalc, 2)
    fCalc = degC*(9/5)+32
    degF = round(fCalc, 2)
    display.scroll(str(degC))
    sleep(1000)
    display.scroll(str(degF))
    sleep(1000)
