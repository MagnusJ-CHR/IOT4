import machine
import time
import uasyncio as asyncio
import screen
from fan import fan_curve
import environmentmanagement as enviro
from transistor import transistor_toggle
from classes import Species,species_dict
from relay import relay_toggle

chosen_species = ""

#Time formatting for valid input
def format_time(sentence,position = 2,character = ":"):
    new_sentence = sentence[:position] + character + sentence[position:]
    return new_sentence
#Relay control
async def relay_schedule_task(relay,start_time,start_state,end_time,end_state):
    global unformatted_time,formatted_time
    formatted_start = format_time(start_time)
    formatted_end = format_time (end_time)
    stored_time = ""
    print(f"Relay {relay} will start schedule from {formatted_start} to {formatted_end} while {start_state}.")
    toggled_end = 0
    toggled_start = 0
    while True:
        current_hour = time.localtime()[3]
        current_minute = time.localtime()[4]
        unformatted_time = (current_hour * 100) + current_minute
        unformatted_time = f"{current_hour:02d}{current_minute:02d}"
        formatted_time = format_time(unformatted_time)
        if formatted_time != stored_time:
            print(f"Current time: {formatted_time}")
        stored_time = formatted_time
        formatted_start = format_time(start_time)
        formatted_end = format_time (end_time)
        if relay == 1:
            if int(start_time) <= int(unformatted_time) <= int(end_time) and toggled_start == 0:
                relay_toggle(relay,start_state)
                toggled_start = 1
                toggled_end= 1
                print(f"Relay {relay} starting schedule from {formatted_start} to {formatted_end} while {start_state}.")
            elif not int(start_time) <= int(unformatted_time) <= int(end_time) and toggled_end == 1:
                relay_toggle(relay,end_state)
                print(f"Ending scheduled relay {relay} that was {start_state} from {formatted_start} to {formatted_end} to {end_state}.")
                toggled_start = 0
                toggled_end = 0
            else:
                pass
        elif relay == 2:
            if int(start_time) <= int(unformatted_time) <= int(end_time) and toggled_start == 0:
                relay_toggle(relay,start_state)
                toggled_start = 1
                toggled_end= 1
                print(f"Relay {relay} starting schedule from {formatted_start} to {formatted_end} while {start_state}.")
            elif not int(start_time) <= int(unformatted_time) <= int(end_time) and toggled_end == 1:
                relay_toggle(relay,end_state)
                print(f"Ending scheduled relay {relay} that was {start_state} from {formatted_start} to {formatted_end} to {end_state}.")
                toggled_start = 0
                toggled_end = 0
            else:
                pass

        await asyncio.sleep(10)
#Starts the tasks       
def start_relay_schedule(relay, chosen_species,start_state = True,end_state = False):
    if relay == 1:
        print(f"Attempting to start schedule for {chosen_species}!")
        schedule_start = species_dict[chosen_species].heat_schedule[0]
        schedule_end = species_dict[chosen_species].heat_schedule[1]
        task_three = asyncio.create_task(relay_schedule_task(1, schedule_start,start_state,schedule_end,end_state))
    if relay == 2:
        print(f"Attempting to start schedule for {chosen_species}!")
        schedule_start = species_dict[chosen_species].light_schedule[0]
        schedule_end = species_dict[chosen_species].light_schedule[1]
        task_four = asyncio.create_task(relay_schedule_task(2,schedule_start,start_state,schedule_end,end_state))

#Screen task and measurements task
async def start_screen_schedule(chosen_species):
    while True:
        screen.environment()
        screen.base_screen(chosen_species)
        await asyncio.sleep(10)


async def start_fan_schedule():
    from screen import low_end_temp,temp,high_end_temp
    fan_curve(low_end_temp,temp,high_end_temp)
    await asyncio.sleep(5)
    

async def start_transistor_schedule():
    from screen import rmoist,hum,high_end_hum,high_end_moist,low_end_hum,low_end_moist
    if low_end_moist <= rmoist <= high_end_moist or rmoist <= high_end_moist:
        transistor_toggle(1,False)
    elif rmoist <= low_end_moist:
        print("Watering!")
        transistor_toggle(1,True)
        asyncio.sleep(2)
    else:
        pass
    
    if low_end_hum <= hum <= high_end_hum or hum <= high_end_hum:
        transistor_toggle(2,False)
    elif rmoist <= low_end_moist:
        print("Humidifying")
        transistor_toggle(2,True)
        asyncio.sleep(2)
    else:
        pass
    
    
    await asyncio.sleep(20)
    
    
    



#Starts singular tasks or functions that start other tasks
async def main(chosen_species):
    #start_fan_schedule()
    start_relay_schedule(1,chosen_species)
    start_relay_schedule(2,chosen_species)
    task_one = asyncio.create_task(start_screen_schedule(chosen_species))
    task_two = asyncio.create_task(start_fan_schedule())
    task_five = asyncio.create_task(start_transistor_schedule())
    
    await asyncio.gather(task_one,task_two,task_five)

def start_schedules(chosen_species):
    asyncio.run(main(chosen_species))
