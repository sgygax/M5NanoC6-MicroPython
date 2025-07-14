# The built-in blue LED.
# - https://docs.m5stack.com/en/core/M5NanoC6

#--------------------------------------------------
import time
import machine

#--------------------------------------------------
# setup
led_blue = machine.Pin(7, machine.Pin.OUT)

#--------------------------------------------------
# loop
while True:
  led_blue.on();
  time.sleep(0.5)

  led_blue.off();
  time.sleep(0.5)
