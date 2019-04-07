from random import random
import machine
import time


class Servo:
    def __init__(self, pin_num):
        self.pin = machine.Pin(pin_num, machine.Pin.OUT)
        self.pwm = machine.PWM(self.pin)
        self.pwm.freq(50)
        self.pwm.duty(0)

    def speed(self, speed):

        if speed == 0:
            self.pwm.duty(0)
            return

        duty = 22 + int(speed * 21)
        duty = max(min(duty, 42), 1)
        self.pwm.duty(duty)


