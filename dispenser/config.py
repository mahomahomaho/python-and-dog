OTA = {'SSID': 'SSID', 
       'password': 'wifipass',
       'wifi_conn_timeout': 10,
       'bind_ip': '10.11.12.1',
       'node_type': 'dispenser'}

BROKER="192.168.1.50"
SSID="SOME_NET"
PASS="some_pass"

NUM_MOVES_PER_DOSE = 1
POS_LEFT = 0
POS_RIGHT = 1
OPEN_TIME = 0.5

try:
    from config_local import *
except:
    pass


