import scheduler
from classes import Species,species_dict
import screen
import relay
from time import sleep
from credentials import chosen_species

scheduler.start_schedules(chosen_species)
try:
    while True:
        sleep(5)
        
       

except KeyboardInterrupt:
    relay_one.value(1)
    relay_two.value(1)