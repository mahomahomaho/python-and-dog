import random
import time

from machine import Pin, Signal
from umqtt.simple import MQTTClient

from . import defs

def run():
   
    pin = Pin(defs.BUTTON_PIN, Pin.IN)
    signal = Signal(pin)

    led = Pin(defs.LED_PIN, Pin.OUT)

    print("connect to broker")

    c = MQTTClient("button", defs.BROKER)
    c.connect()

    print("connected to broker, run main loop")

    last_button = None
    led.value(0)
    while True:

        time.sleep(random.randint(defs.MIN_DELAY, defs.MAX_DELAY))

        led.value(1)

        while not signal.value():
            time.sleep(0.1)

        print("button pressed, send 'treat' to dispenser")

        led.value(0)

        c.publish("luke", "treat")


