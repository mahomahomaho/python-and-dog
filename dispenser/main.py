import network
import usocket

from time import sleep
from servo import Servo

import otacli
import config

if otacli.check():
    print("this line will be never reached")

servo = None

def handle(msg):
    global servo

    if msg == "treat":
        servo.speed(config.TURN_SPEED)
        sleep(config.TURN_TIME)
        servo.speed(0)

        return "OK"
    
    raise Exception("unknown order: %s" % msg)

    # if msg.startswith("speed"):
    #     print("set speed to %s" % msg)
    #     servo.speed(float(msg.decode())/100)

    # if topic == b"duty":
    #     print("set duty to %s" % msg)
    #     servo.pwm.duty(int(msg.decode()))


print("CREATE WIFI AP")
station = network.WLAN(network.AP_IF)
station.active(True)
station.config(essid=config.AP_SSID, authmode=3, password=config.AP_PASS)
ifconfig = station.ifconfig()
station.ifconfig((config.AP_IP, "255.255.255.0", ifconfig[2], config.AP_DNS))
print("IP IS SET")

socket = usocket.socket()
print("A")
addr = ('0.0.0.0', config.LISTEN_PORT)
print("AA")
socket.bind(addr)
print("B")
socket.listen(5)
print("C")

print("run servo")
servo = Servo(config.SERVO_PIN)

print("listen up")
while True:
    conn, addr = socket.accept()
    
    print("conencted by ", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break

        data = data.strip().decode('utf-8')

        try:
            conn.send("RETURNED %s\n\n" % handle(data))
        except Exception as e:
            conn.send("Could not handle '%s': %s\n\n" % (data, e))
