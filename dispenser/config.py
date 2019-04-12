WIFI = {'ap': {'ssid': 'dispenser',
               'pass': 'dispenserpass',
               # if set to None, no ip is set
               'ip': None,
               'dns': None},

        'client': {'ssid': 'some_network',
                   'pass': 'some_pass',
                   # if set to None, no ip is set
                   'ip': None,
                   'dns': None}}

SERVO_PIN = 19
TURN_SPEED = 0.7
SMALL_PORTION_TIME = 0.2

LISTEN_PORT = 2477

VOLTAGE_PIN = 32  # acdc pin
VOLTAGE_RATIO = 51 / 2  # because voltage divider has 51kOhms and 2kOhms

try:
    from config_local import *   # noqa:
except Exception:
    pass


