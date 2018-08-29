import network
import usocket

from time import sleep
from servo import Servo

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

print("CREATE WIFI AP")
station = network.WLAN(network.AP_IF)
station.active(True)
# station.connect(config.SSID, config.PASS)
station.config(essid=config.AP_SSID)
station.config(authmode=3, password=config.AP_PASS)
ifconfig = station.ifconfig()
station.ifconfig((config.AP_IP, "255.255.255.0", ifconfig[2], ifconfig[3]))
print("IP IS SET")

socket = usocket.socket()
print("A")
socket.bind(usocket.getaddrinfo(config.AP_IP, config.LISTEN_PORT))
print("B")
socket.listen()
print("C")

while True:
    x = socket.accept()
    print("after ACCEPT x=%s" % x)


# servo = Servo(config.SERVO_PIN)
#     
# try:
#     while True:
#         c.wait_msg()
# finally:
#     c.disconnect()
# 
