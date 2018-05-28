OTA = {'SSID': 'SSID', 
       'password': 'wifipass',
       'wifi_conn_timeout': 10,
       'bind_ip': '10.11.12.1',
       'node_type': 'dispenser'}

BROKER="192.168.1.50"
SSID="SOME_NET"
PASS="some_pass"

NUM_MOVES_PER_DOSE = 1
TURN_FROM = 0.0
TURN_TO = 0.9
TURN_FORWARD=0.3
TURN_BACK=0.1
SERVO_PIN = 19

try:
    from config_local import *
except:
    pass


