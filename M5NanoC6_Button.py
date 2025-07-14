# The built-in button.
# - https://docs.m5stack.com/en/core/M5NanoC6

#--------------------------------------------------
import time
import machine

#--------------------------------------------------
# setup
button = machine.Pin(9, machine.Pin.IN)

#--------------------------------------------------
# loop
while True:
  button_state = button.value()

  print(button_state)
  
  time.sleep(0.1)