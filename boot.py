import network
import credentials as cred

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def connect_net():
    wlan.connect(cred.wifi_ssid, cred.wifi_password)
    print("Attempting to connect")
    while not wlan.isconnected():
        pass
    print("Connected to Wi-Fi:", wlan.ifconfig())

try:
    connect_net()
    print("Succeeded!")
except KeyboardInterrupt:
    print("Exiting")