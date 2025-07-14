# The built-in Neopixel RGB-LED.
# - https://docs.m5stack.com/en/core/M5NanoC6

#--------------------------------------------------
import time
import machine
import neopixel

#--------------------------------------------------
# setup
rgb_enable = machine.Pin(19, machine.Pin.OUT)
rgb_enable.on();

rgb = neopixel.NeoPixel(machine.Pin(20), 1)

#--------------------------------------------------
# loop
while True:
    # R=100% G=0%, B=0%
    rgb[0] = (255, 0, 0)
    rgb.write()
    time.sleep(0.500)
    
    # R=0% G=100%, B=0%
    rgb[0] = (0, 255, 0)
    rgb.write()
    time.sleep(0.500)
    
    # R=0% G=0%, B=100%
    rgb[0] = (0, 0, 255)
    rgb.write()
    time.sleep(0.500)
    
    # R=100% G=100%, B=100%
    rgb[0] = (255, 255, 255)
    rgb.write()
    time.sleep(0.500)
    
    # R=0% G=0%, B=0%
    rgb[0] = (0, 0, 0)
    rgb.write()
    time.sleep(0.500)