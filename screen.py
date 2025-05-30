from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin,ADC
from time import sleep
import math
import dhtsensor
from classes import species_dict
import relay
import fan 
import transistor
import scheduler
from credentials import chosen_species
import dht
from machine import Pin,ADC

dht_pin = Pin(4)  # GPIO 4
sensor = dht.DHT11(dht_pin)

# Define the ADC pin
adc_pin = ADC(Pin(32))  # GPIO 32
adc_pin.width(ADC.WIDTH_12BIT)  # Set resolution (0-4095)
adc_pin.atten(ADC.ATTN_11DB)  # Set attenuation for full range (0-3.3V)

def environment():
    global temp,hum,moisture,rmoist
    sensor.measure()  # Trigger measurement
    temp = sensor.temperature()
    hum = sensor.humidity()
    moisture = adc_pin.read()
    rmoist = round(moisture / 3100 * 100, 2)
    return temp,hum,moisture,rmoist




moisture = 0
rmoist = 0
temp = 0
hum = 0


transistor_one = Pin(22,Pin.OUT)
transistor_two = Pin(23,Pin.OUT)

tft_CS = 5
tft_RESET= 16
tft_A0 = 18
tft_SDA=13
tft_SCK=14

spi = SPI(1, baudrate=20000000, polarity=0, phase=0,miso=None)
tft=TFT(spi,tft_A0,tft_RESET,tft_CS)
tft.initr()
tft.rgb(True)

def base_screen(user_species):
    tft.fill(TFT.BLACK)
    header_box()
    temperature_box()
    humidity_box()
    ground_moisture_box()
    relays_box()
    transistor_box()
    fan_box()
    dividers_box()

        
    
    
    
def in_range(lower_end,value,higher_end,sensor):
    if sensor == "temperature":
        state = lower_end <= value <= higher_end
        if state == True:
            return TFT.GREEN
        elif value >= higher_end:
            return TFT.RED
        else:
            return TFT.BLUE
    elif sensor == "humidity":
        state = lower_end <= value <= higher_end
        if state == True:
            return TFT.GREEN
        elif value >= higher_end:
            return TFT.BLUE
        else:
            return TFT.RED
    
    else:
        state = lower_end <= value <= higher_end
        if state == True:
            return TFT.GREEN
        elif value >= higher_end:
            return TFT.BLUE
        else:
            return TFT.RED
def in_use(device):
    if device == 1:
        return TFT.RED
    else:
        return TFT.GREEN
    
def fan_color(fan_speed):
    fan_color = 75 <= fan_speed <= 101
    if fan_color == True:
        return TFT.RED
    elif 25 <= fan_speed <= 75:
        return TFT.NAVY
    else:
        return TFT.GREEN


##Temp
low_end_temp = species_dict[chosen_species].temperature[0]
high_end_temp = species_dict[chosen_species].temperature[1]
##Hum
low_end_hum = species_dict[chosen_species].humidity[0]
high_end_hum = species_dict[chosen_species].humidity[1]
##Hum
low_end_moist = species_dict[chosen_species].ground_moisture[0]
high_end_moist = species_dict[chosen_species].ground_moisture[1]

def header_box():
    tft.text((0, 0), f"{species_dict[chosen_species].name}", TFT.GREEN, sysfont, 1)

def temperature_box():
    tft.text((0, 20), "Expected temp", TFT.WHITE, sysfont, 1)
    tft.text((85, 20), f"{low_end_temp}" + "/" + f"{high_end_temp}", TFT.WHITE, sysfont, 1)
    tft.text((0, 30), "Current temp", TFT.WHITE, sysfont, 1)
    temp_color = in_range(low_end_temp,temp,high_end_temp,"temperature")
    tft.text((85, 30), f'{temp}C', temp_color , sysfont, 1)
    
def humidity_box():
    tft.text((0, 50), "Expected hum", TFT.WHITE, sysfont, 1)
    tft.text((85, 50), f"{low_end_hum}" + "/" + f"{high_end_hum}", TFT.WHITE, sysfont, 1)
    tft.text((0, 60), "Current hum", TFT.WHITE, sysfont, 1)
    hum_color = in_range(low_end_hum,hum,high_end_hum,"humidity")
    tft.text((85, 60), f'{hum}%', hum_color , sysfont, 1)
    
def ground_moisture_box():
    tft.text((0, 80), "Expected moist", TFT.WHITE, sysfont, 1)
    tft.text((85, 80), f"{low_end_moist}" + "/" + f"{high_end_moist}", TFT.WHITE, sysfont, 1)
    tft.text((0, 90), "Current moist", TFT.WHITE, sysfont, 1)
    hum_color = in_range(low_end_moist,rmoist,high_end_moist,"moisture")
    tft.text((85, 90), f'{rmoist}%', hum_color , sysfont, 1)
    
def ground_moisture_box():
    tft.text((0, 80), "Expected moist", TFT.WHITE, sysfont, 1)
    tft.text((85, 80), f"{low_end_moist}" + "/" + f"{high_end_moist}", TFT.WHITE, sysfont, 1)
    tft.text((0, 90), "Current moist", TFT.WHITE, sysfont, 1)
    hum_color = in_range(low_end_moist,rmoist,high_end_moist,"moisture")
    tft.text((85, 90), f'{rmoist}%', hum_color , sysfont, 1)

def relays_box():
    tft.text((90, 102), "Relays", TFT.WHITE, sysfont, 1)
    tft.text((110, 113), f"R1", in_use(relay.relay_one_status), sysfont, 1)
    tft.text((110, 123), f"R2", in_use(relay.relay_two_status), sysfont, 1)
    
def transistor_box():
    tft.text((60, 130), "Transistors", TFT.WHITE, sysfont, 1)
    tft.text((95, 142), f"Pump", in_use(transistor.transistor_one_status), sysfont, 1)
    tft.text((95, 152), f"Mist", in_use(transistor.transistor_two_status), sysfont, 1)
    
def fan_box():
    tft.text((0, 102), "Fan", TFT.WHITE, sysfont, 1)
    tft.text((0, 113), f"{fan.speed}", fan_color(fan.speed), sysfont, 1)
    #tft.line((0,100),(128,100), TFT.WHITE)

def dividers_box():
    #Line between temp and title / species section
    tft.line((0,15),(128,15), TFT.WHITE)
    #Line between temp and humidity
    tft.line((0,45),(128,45), TFT.WHITE)
    #Line between Humid and moist section
    tft.line((0,75),(128,75), TFT.WHITE)
    #Line between moisture and fan section
    tft.line((0,100),(128,100), TFT.WHITE)
    


