import logging
import machine
import os
import picoweb
import uasyncio
from machine import ADC, Pin

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

adc = ADC(Pin(config.VOLTAGE_PIN))


app = picoweb.WebApp(__name__)
# debug values:
# -1 disable all logging
# 0 (False) normal logging: requests and errors
# 1 (True) debug logging
# 2 extra debug logging


def voltage():
    global adc
    return adc.read() / 4096 * config.VOLTAGE_RATIO


@app.route("/voltage")
def get_voltage(req, resp):
    yield from picoweb.jsonify(resp, {'voltage': voltage()})


@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from app.render_template(resp, "index.tpl", (req, voltage()))


@app.route("/clear_templates")
def clear_templates(req, resp):
    for x in os.listdir("templates"):
        if not x.endswith(".py"):
            continue
        f = "templates/%s" % x
        os.unlink(f)
        logger.info("removed template %s", f)
    headers = {"Location": ".."}
    yield from picoweb.start_response(resp, status="303", headers=headers)


@app.route("/treat", method=["POST"])
def treat(req, resp):
    global servo

    if req.method != "POST":
        logger.debug("method = %s, skipping", req.method)
        return

    yield from req.read_form_data()

    portion_size = float(req.form.get("portion", "2"))

    logger.debug("set speed to %s", config.TURN_SPEED)
    servo.speed(config.TURN_SPEED)
    sleeptime = portion_size * config.SMALL_PORTION_TIME
    logger.debug("wait %s seconds", sleeptime)
    yield from uasyncio.sleep(sleeptime)
    logger.debug("set speed to 0")
    servo.speed(0)
    logger.debug("done")

    headers = {"Location": ".."}
    yield from picoweb.start_response(resp, status="303", headers=headers)


app.run(host='0.0.0.0', port=80, debug=2)
