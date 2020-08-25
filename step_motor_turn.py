import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PINS = [18, 17, 27, 22]

for PIN in PINS:
    GPIO.setup(PIN, GPIO.OUT)
    
sequence = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1],
    ]

import sys

_input = sys.argv

try:
    for i in range(512):
        for half_step in range(8):
            for pin in range(4):
                GPIO.output(PINS[pin], sequence[half_step][pin])
            time.sleep(0.001)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

