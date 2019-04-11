import logging
import network
import machine
import picoweb
import uasyncio
import usocket
import time

from time import sleep
from servo import Servo

import config
import conn

servo = None
logger = logging.getLogger(__name__)


def blink(msg=None, static={'v': 0}):
    lednum = getattr(config, "BLINK_LED", 2)
    led = machine.Pin(lednum, machine.Pin.OUT)
    static['v'] = (static['v'] + 1) % 2
    led.value(static['v'])
    if msg:
        print(msg)



logging.basicConfig(level=logging.DEBUG)
conn.init_wifi()

logging.info("run servo")
servo = Servo(config.SERVO_PIN)


app = picoweb.WebApp(__name__)
# debug values:
# -1 disable all logging
# 0 (False) normal logging: requests and errors
# 1 (True) debug logging
# 2 extra debug logging

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from app.render_template(resp, "index.tpl", (req,))


@app.route("/treat", method=["POST"])
def treat(req, resp):
    global servo
    
    servo.speed(config.TURN_SPEED)
    sleep(config.TURN_TIME)
    servo.speed(0)

    headers = {"Location": ".."}
    yield from picoweb.start_response(resp, status="303", headers=headers)


app.run(host='0.0.0.0', port=80, debug=2)
