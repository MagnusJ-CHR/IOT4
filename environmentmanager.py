import dht
from machine import Pin,ADC

dht_pin = Pin(4)
sensor = dht.DHT11(dht_pin)

moisture = 0
rmoist = 0
temp = 0
hum = 0

adc_pin = ADC(Pin(32))
adc_pin.width(ADC.WIDTH_12BIT)
adc_pin.atten(ADC.ATTN_11DB)

def environment():
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    moisture = adc_pin.read()
    rmoist = round(moisture / 3100 * 100, 2)
    return temp,hum,moisture,rmoist

temperature_list = environment()
print(temperature_list)