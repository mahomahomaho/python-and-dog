import network
from time import sleep
from servo import Servo

from umqtt.simple import MQTTClient

import otacli
import config

if otacli.check():
    print("this line will be never reached")

servo = None

def sub_cb(topic, msg):
    global servo

    if msg == b"treat":
        print("turn %s times" % config.NUM_MOVES_PER_DOSE)
        for x in range(config.NUM_MOVES_PER_DOSE):
            print("turn %s" % x)
            pos = config.TURN_FROM
            print("start from %s" % pos)
            servo.set(pos)
            while pos < config.TURN_TO:
                pos += config.TURN_FORWARD
                print("forward to %s" % pos)
                servo.set(pos)
                pos -= config.TURN_BACK
                print("back to %s" % pos)
                servo.set(pos)

    if topic == b"setpos":
        print("set pos to %s" % msg)
        servo.set(float(msg.decode())/100)
    
    if topic == b"freq":
        print("set freq to %s" % msg)
        servo.pwm.freq(int(msg.decode()))
    
    if topic == b"duty":
        print("set duty to %s" % msg)
        servo.pwm.duty(int(msg.decode()))


print('WIFI connecting')
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(config.SSID, config.PASS)

while not station.isconnected():
    print("not connected to wifi")
    sleep(1)

print("connect to broker")
c = MQTTClient("dispenser", config.BROKER)

c.set_callback(sub_cb)
c.connect()
    
c.subscribe("dispenser")
c.subscribe("freq")
c.subscribe("duty")
c.subscribe("setpos")

servo = Servo(config.SERVO_PIN)
    
try:
    while True:
        c.wait_msg()
finally:
    c.disconnect()

