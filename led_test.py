from RPi import GPIO
from time import sleep

import sys

_input = sys.argv[1:]

class LED:

    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
    
    def flash(self, duration):
        GPIO.output(self.pin, GPIO.HIGH)
        sleep(duration)

        GPIO.output(self.pin, GPIO.LOW)
        GPIO.cleanup()


try:
    for i in range(int(_input[2])):
        LED(int(_input[0])).flash(float(_input[1]))

        try:
            sleep(_input[3])
        except:
            sleep(1)

except:
    LED(int(_input[0])).flash(float(_input[1]))

