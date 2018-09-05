OTA = {'SSID': 'SSID', 
       'password': 'wifipass',
       'wifi_conn_timeout': 10,
       'bind_ip': '10.11.12.1',
       'node_type': 'dispenser'}

AP_SSID="dispenser"
AP_PASS="dispenser_pass"
AP_IP="192.168.4.10"
AP_DNS='8.8.8.8'

SERVO_PIN = 19
TURN_SPEED = 0.2
TURN_TIME = 3

LISTEN_PORT = 2477

try:
    from config_local import *
except:
    pass


