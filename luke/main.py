import time

from umqtt.simple import MQTTClient

from .servo import Servo
from . import defs

servo = None

def sub_cb(topic, msg):
    global servo

    if msg == b"treat":
        print("open dispenser for a while")
        servo.set(defs.STATE_OPEN)
        time.sleep(defs.OPEN_TIME)
        servo.set(defs.STATE_CLOSED)

    if topic == b"setpos":
        print("DEBUG set servo to pos %s" % msg)
        servo.set(float(msg.decode()))
        

def run_server():
    global servo
    
    servo = Servo(defs.SERVO_PIN)

    print("connect to broker")

    c = MQTTClient("dispenser", defs.BROKER)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe("luke")
    c.subscribe("setpos")

    print("connected to broker, run main loop")

    try:
        while True:
            c.wait_msg()
    finally:
        c.disconnect()


    

    
