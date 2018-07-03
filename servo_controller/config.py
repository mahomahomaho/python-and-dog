OTA = {'SSID': 'SSID', 
       'password': 'wifipass',
       'wifi_conn_timeout': 10,
       'bind_ip': '10.11.12.1',
       'node_type': 'scontrol'}

SERVO_PIN = 19
ADAC_PINS = (35, 36)
NEUTRAL_V = 1.5

try:
    from config_local import *
except:
    pass


