import random
from classes import species_dict
wifi_ssid = ""
wifi_password = ""

global chosen_species
chosen_species = random.choice(list(species_dict.keys()))


