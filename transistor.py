from machine import Pin
from time import sleep

transistor_one = Pin(22,Pin.OUT)
transistor_two = Pin(23,Pin.OUT)

transistor_one.value(0)
transistor_two.value(0)

transistor_one_status = 0
transistor_two_status = 0


def transistor_toggle(value,state):
    global transistor_one_status, transistor_two_status
    transistor = value
    print(f"Chosen to toggle transistor {transistor} to {state}")
    if value == 1:
        if state == True:
            transistor_one.value(1)
            print("Transistor one on.")
            transistor_one_status = 1
        else:
            transistor_one.value(0)
            print("Transistor one off.")
            transistor_one_status = 0
        
    elif value == 2:
        if state == True:
            transistor_two.value(1)
            print("Transistor two on.")
            transistor_two_status = 1
        
        else:
            transistor_two.value(1)
            print("Transistor two off.")
            transistor_two_status = 0
    else:
        pass