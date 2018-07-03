from time import sleep
from servo import Servo
from machine import Pin, ADC

import otacli
import config

if otacli.check():
    print("this line will be never reached")

servo = None


servo = Servo(config.SERVO_PIN)
adcs = [ADC(Pin(x)) for x in config.ADAC_PINS]
    
while True:
    sleep(0.1)
    v1, v2 = [x.read() for x in adcs]
    v =  0.53 * (v1 + v2*7.0) / 1960.0
    print("v=", v)
    servo.speed(config.NEUTRAL_V - v)

