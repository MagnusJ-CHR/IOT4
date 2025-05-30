import dht
from machine import Pin

dht_pin = Pin(4) 
sensor = dht.DHT11(dht_pin)

def temp_and_hum():
    sensor.measure() 
    temp = sensor.temperature()
    hum = sensor.humidity()
    return temp,hum