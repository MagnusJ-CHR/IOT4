import network
import credentials

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(credentials.SSID, credentials.PASSWORD)

    while not wlan.isconnected():
        pass

    print("Connected to Wi-Fi:", wlan.ifconfig())

connect_wifi()
