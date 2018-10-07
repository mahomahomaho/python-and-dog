OTA = {'SSID': 'SSID', 
       'password': 'wifipass',
       'wifi_conn_timeout': 10,
       'bind_ip': '10.11.12.1',
       'node_type': 'dispenser'}

AP_SSID="dispenser"
AP_PASS="dupadupa"
AP_IP="192.168.4.10"
AP_DNS='8.8.8.8'

SERVO_PIN = 19
TURN_SPEED = 0.7
TURN_TIME = 0.5

LISTEN_PORT = 2477

try:
    from config_local import *
except:
    pass


