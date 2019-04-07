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
TURN_SPEED = 0.8
TURN_TIME = 0.7

LISTEN_PORT = 2477

try:
    from config_local import *
except:
    pass


