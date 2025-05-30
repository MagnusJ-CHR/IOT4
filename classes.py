temp = 0
hum = 0


class Species:
    def __init__(self,name,species,descriptor,temperature,humidity,light_schedule,heat_schedule,ground_moisture):
        self.name = name
        self.species = species
        self.descriptor = descriptor
        self.temperature = temperature
        self.humidity = humidity
        self.light_schedule = light_schedule
        self.heat_schedule = heat_schedule
        self.ground_moisture = ground_moisture
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Descriptor: {self.descriptor}")
        print(f"Expected temperature: {self.temperature}")
        print(f"Expected humidity: {self.humidity}")
        print(f"Expected light schedule: {self.light_schedule}")
        print(f"Expected heat schedule: {self.heat_schedule}")
        print(f"Expected heat schedule: {self.ground_moisture}")    

species_dict = {
    "Bearded Dragon": Species("Bearded Dragon", "Pogona vitticeps", "Can run on two legs when escaping predators.", (25, 35), (30, 40), ["0800", "2000"], ["0730", "2200"], (10, 20)),
    "Leopard Gecko": Species("Leopard Gecko", "Eublepharis macularius", "Can regenerate its tail after dropping it.", (24, 30), (30, 40), ["0900", "2100"], ["0800", "2200"], (20, 40)),
    "Crested Gecko": Species("Crested Gecko", "Correlophus ciliatus", "Was thought to be extinct until rediscovered in 1994.", (22, 28), (50, 70), ["0800", "2000"], ["0700", "2200"], (50, 70)),
    "Ball Python": Species("Ball Python", "Python regius", "Rolls into a ball when feeling threatened.", (26, 32), (50, 60), ["0900", "2100"], ["0800", "2200"], (40, 60)),
    "Corn Snake": Species("Corn Snake", "Pantherophis guttatus", "Has a belly pattern resembling corn kernels.", (24, 30), (40, 50), ["0800", "2000"], ["0700", "2200"], (30, 50)),
    "Red-Eyed Tree Frog": Species("Red-Eyed Tree Frog", "Agalychnis callidryas", "Uses its bright colors to startle predators.", (22, 28), (70, 80), ["0800", "2000"], ["0700", "2200"], (70, 90)),
    "Pacman Frog": Species("Pacman Frog", "Ceratophrys ornata", "Consumes prey almost as large as itself.", (24, 30), (60, 80), ["0900", "2100"], ["0800", "2130"], (60, 80)),
    "Axolotl": Species("Axolotl", "Ambystoma mexicanum", "Can regenerate limbs, spinal cord, and parts of its brain.", (16, 20), (70, 80), ["0800", "2000"], ["0700", "2200"], (80, 100)),
    "Fire-Bellied Toad": Species("Fire-Bellied Toad", "Bombina orientalis", "Flips onto its back to display warning colors.", (22, 26), (60, 80), ["0800", "2000"], ["0700", "2200"], (60, 80)),
    "Green Anole": Species("Green Anole", "Anolis carolinensis", "Changes color based on mood and temperature.", (24, 30), (50, 70), ["0800", "2000"], ["0700", "2200"], (40, 60)),
    "Tokay Gecko": Species("Tokay Gecko", "Gekko gecko", "Has one of the loudest calls among geckos.", (26, 32), (60, 80), ["0900", "2100"], ["0800", "2200"], (50, 70)),
    "Blue-Tongue Skink": Species("Blue-Tongue Skink", "Tiliqua scincoides", "Displays its blue tongue to deter predators.", (26, 32), (40, 60), ["0800", "2000"], ["0700", "2200"], (30, 50)),
    "Veiled Chameleon": Species("Veiled Chameleon", "Chamaeleo calyptratus", "Stores water in its casque-shaped head crest.", (24, 30), (50, 70), ["0800", "2000"], ["0700", "2200"], (50, 70)),
    "Panther Chameleon": Species("Panther Chameleon", "Furcifer pardalis", "Can move its eyes independently in different directions.", (24, 30), (60, 80), ["0800", "2000"], ["0700", "2200"], (60, 80)),
    "Day Gecko": Species("Day Gecko", "Phelsuma grandis", "Licks its own eyes to keep them clean.", (24, 30), (60, 80), ["0800", "2000"], ["0700", "2200"], (60, 80)),
    "Rosy Boa": Species("Rosy Boa", "Lichanura trivirgata", "Rolls into a ball to hide when threatened.", (26, 32), (40, 50), ["0900", "2100"], ["0800", "2200"], (30, 50)),
    "Milk Snake": Species("Milk Snake", "Lampropeltis triangulum", "Mimics the venomous coral snake for protection.", (24, 30), (40, 50), ["0800", "2000"], ["0700", "2200"], (30, 50)),
    "Green Tree Python": Species("Green Tree Python", "Morelia viridis", "Starts life as bright yellow or red before turning green.", (26, 32), (60, 80), ["0800", "2000"], ["0700", "2200"], (50, 70)),
    "Dart Frog": Species("Poison Dart Frog", "Dendrobates tinctorius", "Some species are highly toxic in the wild.", (22, 28), (70, 90), ["0800", "2000"], ["0700", "2200"], (70, 90)),
    "Red-Footed Tortoise": Species("Red-Footed Tortoise", "Chelonoidis carbonarius", "Recognizes its owner and responds to its name.", (24, 30), (50, 70), ["0800", "2000"], ["0700", "2200"], (50, 70)),
    "Russian Tortoise": Species("Russian Tortoise", "Agrionemys horsfieldii", "Digs burrows to escape extreme temperatures.", (26, 32), (30, 50), ["0800", "2000"], ["0700", "2200"], (20, 40)),
    "Asian Forest Scorpion": Species("Asian Forest Scorpion", "Heterometrus spp.", "Glows under UV light due to its exoskeleton.", (24, 30), (60, 80), ["0800", "2000"], ["0700", "2200"], (60, 80)),
    "Emperor Scorpion": Species("Emperor Scorpion", "Pandinus imperator", "One of the largest scorpions but relatively docile.", (24, 30), (60, 80), ["0800", "2000"], ["0700", "2200"], (60, 80)),
    "Giant African Millipede": Species("Giant African Millipede", "Archispirostreptus gigas", "Has over 250 legs but moves slowly.", (22, 28), (70, 90), ["0800", "2000"], ["0700", "2200"], (70, 90))
}


