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
        servo.speed(config.TURN_SPEED)
        sleep(config.TURN_TIME)
        servo.speed(0)

    if topic == b"speed":
        print("set speed to %s" % msg)
        servo.speed(float(msg.decode())/100)
    
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
c.subscribe("duty")
c.subscribe("speed")

servo = Servo(config.SERVO_PIN)
    
try:
    while True:
        c.wait_msg()
finally:
    c.disconnect()

