from machine import Pin, PWM
import time
import dht
from classes import species_dict
from credentials import chosen_species

fan = PWM(Pin(21))
fan.freq(25000)
fan.duty_u16(0)

speed = 0

def fan_pwm(percentage):
    global speed
    duty = int((percentage / 100) * 65535)
    fan.duty_u16(duty)
    print(f"Fan set to {percentage}% speed")
    speed = percentage
    return speed

def fan_curve(low,temp,high):
    if temp < low or low <= temp <= high:
        fan_pwm(0)
    elif high + 5 <= temp:
        fan_pwm(100)
    elif high + 3 <= temp:
        fan_pwm(50)
    elif high + 1 <= temp:
        fan_pwm(25)


