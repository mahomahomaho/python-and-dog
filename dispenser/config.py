OTA = {'SSID': 'SSID', 
       'password': 'wifipass',
       'wifi_conn_timeout': 10,
       'bind_ip': '10.11.12.1',
       'node_type': 'dispenser'}

BROKER="dlaptop.lan"
SSID="SOME_NET"
PASS="some_pass"

SERVO_PIN = 19
TURN_SPEED = 0.2
TURN_TIME = 3

try:
    from config_local import *
except:
    pass


