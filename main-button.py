import network
import time

from luke import defs, client

print('connecting')
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(defs.WIFI_SSID, defs.WIFI_PASS)

while not station.isconnected():
    print("not connected to wifi")
    time.sleep(1)

print("connected")

client.run()
