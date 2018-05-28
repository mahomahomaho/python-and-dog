from random import random
import machine
import time

class Servo:
    def __init__(self, pin_num):
        self.pin = machine.Pin(pin_num, machine.Pin.OUT)
        self.pwm = machine.PWM(self.pin)
        self.pwm.freq(50)
        self.pwm.duty(0)
        self.pos = None

    def set(self, pos):
        ftime = 1.0
        if self.pos is None:
            sleeptime = ftime
        else:
            sleeptime = ftime * abs(pos - self.pos)
        self.pos = pos

        duty = int(40 + (115-40)*pos)
        self.pwm.duty(duty)

        print("sleeptime", sleeptime)

        time.sleep(sleeptime)
        self.pwm.duty(0)


