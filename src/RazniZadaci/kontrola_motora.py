from microbit import *                                      

while True:
    if button_a.is_pressed():
        pin0.write_digital(1)
    if button_b.is_pressed():
        pin0.write_digital(0)
