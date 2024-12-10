from microbit import *

while True:
    if accelometer.was_gesture("shake"):
        pasos =+ 1

    if button_b.is_pressed():
        pasos=0
        display.show("R")

    if button_a.is_pressed():
        print(str(pasos))