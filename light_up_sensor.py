from RPi import GPIO
import time

import sys

_input = sys.argv[1:]

GREEN = 17
BLUE = 27
RED = 22

class Light:
    def __init__(self, ECHO):
        GPIO.setmode(GPIO.BCM)
        self.ECHO = ECHO

        GPIO.setup(self.ECHO, GPIO.OUT)
       
    def on(self):
        GPIO.output(self.ECHO, GPIO.HIGH)


class Sensor:
    def __init__(self, ECHO, TRIG=4):
        GPIO.setwarnings(False)
        GPIO.cleanup()

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
        
        from termcolor import colored
        
        if dist >= 12:
            pass
        elif dist >= 2:
            Light(GREEN).on()
            print(colored(f"{dist} meters", "green"))
        elif 2 > dist > 1:
            Light(BLUE).on()
            print(colored(f"{dist} meters", "blue"))
        else:
            Light(RED).on()
            if dist == 1:
                print(f"{dist} meter")        
            else:
                print(colored(f"{dist} meters", "red"))

        #dist = round(dist, 1)


try: 
    if _input[0] == "calc_dist":
        while True:
            try:
                Sensor(_input[1], _input[2]).calc_dist()
            except IndexError:
                Sensor(_input[1]).calc_dist()
                try:
                    time.sleep(0.1)
                except KeyboardInterrupt:
                    GPIO.cleanup()
                    quit()
    else:
        print("Invalid command.")

except IndexError:
    print("This requires at least 2 inputs.")

