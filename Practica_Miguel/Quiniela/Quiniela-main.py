from microbit import *
import random

    
while True:
    valor= random.randrange(3)
    
    if button_a.is_pressed():
        if valor == 1:
            display.show("1")
        elif valor ==2:
            display.show("X")
        else:
            display.show("2")

    if button_b.is_pressed():
        display.clear()