from random import random
import machine

class Servo:
    def __init__(self, pin_num):
        self.pin = machine.Pin(pin_num, machine.Pin.OUT)
        self.pwm = machine.PWM(self.pin)
        self.pwm.freq(100)

    def set(self, pos):
        duty = int(40 + (200-40)*pos)
        self.pwm.duty(duty)
