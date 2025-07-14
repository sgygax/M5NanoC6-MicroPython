# The built-in blue LED and pulse-width modulation (PWM).
# - https://docs.m5stack.com/en/core/M5NanoC6

#--------------------------------------------------
import time
import machine

#--------------------------------------------------
# setup
led_blue = machine.PWM(machine.Pin(7))

led_blue.duty(0)

#--------------------------------------------------
# loop
while True:
    # 0..100%
    for tg in range(0, 1024, 1):
        led_blue.duty(tg)
        time.sleep(0.002)

    # 100..0%
    for tg in range(1023, -1, -1):
        led_blue.duty(tg)
        time.sleep(0.002)
