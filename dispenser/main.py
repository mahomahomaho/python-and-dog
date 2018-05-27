from time import sleep
from servo import Servo

from umqtt.simple import MQTTClient

import config

servo = None

def sub_cp(topic, msg):
    global servo

    if msg == b"treat":
        print("open dispenser for a while")
        for __ in range(config.NUM_MOVES_PER_DOSE):
            servo.set(config.POS_LEFT)
            time.sleep(config.POS_TIME)
            servo.set(config.POS_RIGHT)
            time.sleep(config.POS_TIME)


print("connect to broker")
c = MQTTClient("dispenser", config.BROKER)

c.set_callback(sub_cb)
c.connect()

servo = Servo(config.SERVO_PIN)

