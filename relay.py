import machine
import time
import uasyncio as asyncio

relay_one = machine.Pin(33, machine.Pin.OUT)

relay_two = machine.Pin(25, machine.Pin.OUT)

relay_one.value(1)
relay_two.value(1)
relay_one_status = 0
relay_two_status = 0

def relay_toggle(value,status):
    global relay_one_status,relay_two_status
    if value == 1:
        if status == True:
            relay_one.value(not status)
            print(f"Relay {value} turned on.")
            return relay_one_status
        else:
            relay_one.value(not status)
            print(f"Relay {value} turned off.")
            return relay_one_status
            
    else:
        if status == True:
            relay_two.value(not status)
            print(f"Relay {value} turned on.")
            return relay_two_status
        else:
            relay_two.value(not status)
            print(f"Relay {value} turned off.")
            return relay_two_status

