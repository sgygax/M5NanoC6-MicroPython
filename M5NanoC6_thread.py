# An example of how to use _thread with 3 tasks.
# - https://docs.m5stack.com/en/core/M5NanoC6

#--------------------------------------------------
import time
import machine
import neopixel
import _thread

#--------------------------------------------------
def Task_2():
    led_blue = machine.PWM(machine.Pin(7))

    led_blue.duty(0)

    while True:
        # 0..100%
        for tg in range(0, 1024, 1):
            led_blue.duty(tg)
            time.sleep(0.002)

        # 100..0%
        for tg in range(1023, -1, -1):
            led_blue.duty(tg)
            time.sleep(0.002)
        
#--------------------------------------------------
def Task_3():
    rgb_enable = machine.Pin(19, machine.Pin.OUT)
    rgb_enable.on();

    rgb = neopixel.NeoPixel(machine.Pin(20), 1)

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

#--------------------------------------------------
# setup
_thread.start_new_thread(Task_2, ())
_thread.start_new_thread(Task_3, ())

#--------------------------------------------------
# loop
while True:
  print("Hallo Welt...")
  time.sleep(1)