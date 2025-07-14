# The built-in infrared (IR) LED.
# - https://docs.m5stack.com/en/core/M5NanoC6

#--------------------------------------------------
import time
import machine

#--------------------------------------------------
# setup
led_ir = machine.Pin(3, machine.Pin.OUT)

#--------------------------------------------------
# loop
while True:
  led_ir.on();
  time.sleep(0.5)

  led_ir.off();
  time.sleep(0.5)