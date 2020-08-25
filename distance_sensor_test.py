from RPi import GPIO
import time

import sys

_input = sys.argv[1:]

class Sensor:
    
    def __init__(self, ECHO, TRIG=4):
        self.ECHO = int(ECHO)
        self.TRIG = int(TRIG)

    def calc_dist(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

        GPIO.output(self.TRIG, True)
        time.sleep(0.0001)
        GPIO.output(self.TRIG, False)
        
        while GPIO.input(self.ECHO) == False:
            start = time.time()

        while GPIO.input(self.ECHO) == True:
            end = time.time()
        
        GPIO.cleanup()

        diff_time = end - start
        
        # Distance in meters.
        dist = diff_time / 0.0058

        #dist = round(dist, 1)

        if dist == 1:
            print(f"{dist} meter")
        else:
            print(f"{dist} meters")

try: 
    if _input[0] == "calc_dist":
        #while True:
        try:
            Sensor(_input[1], _input[2]).calc_dist()
        except IndexError:
            Sensor(_input[1]).calc_dist()
        time.sleep(0.01)
    else:
        print("Invalid command.")

except IndexError:
    print("This requires at least 2 inputs.")

