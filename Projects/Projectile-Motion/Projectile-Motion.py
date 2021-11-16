import math
import os
from ExperimentalData import Experimentaldata
from pathlib import Path
import json
# gun = 'ak-101'
# caliber = '5.56x45 mm'
# ammunition = 'Warmageddon'
# Velocity_ms = 910

# building = 'Minillas South Tower'
# buildingheight = 243.69

# gravity_Ms = 9.81

# import math



def Projectilefunction(experimentaldata: Experimentaldata):
    
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

    planet = planets.index(experimentaldata.planet)

    time_s = math.sqrt((2 * experimentaldata.buildingheight) / g_ms2[planet])
    distance_m = (experimentaldata.velocity_ms * time_s)

    print(f"The gun selected for this experiment is {experimentaldata.gun}. the caliber of {experimentaldata.gun} is {experimentaldata.caliber}, and the ammunition of the {experimentaldata.gun} is {experimentaldata.ammunition}. The spped of the a the ammunition is {experimentaldata.velocity_ms}.")
    print(f'the building that we are going to use is the {experimentaldata.building} in sanjuan, and the height of the {experimentaldata.building} is {experimentaldata.buildingheight}. Also the distance is going to be {distance_m} ')
    print('This day we were lucky that there is no air resistance.')

# Convert your script parameters into a single Json object
# experimentaldata = (

# "gun" : "Ak 101",
# "caliber" : "5.56x45 mm",
# "ammunition" : "Warmageddon",
# 'building' : "Minillas South Tower",
# "Velocity_ms" : "910",
# "buildingheight" : "243.69"
# "gravity_Ms" : "9.81"

# )

# experimentaldata = ExperimentalData("ak 101", "5.56x45 mm", "Warmageddon", 910, "Minilas South Tower", 243.69, 9.81)

myDataset = [
Experimentaldata("ak-101", "5.56x46 mm", "warmageddon", 910, "Minillas South Tower", 243.69, "Earth"),
Experimentaldata("ak-101", "5.56x46 mm", "M995", 1013, "Minillas South Tower", 243.69, "Mars"),
Experimentaldata("ak-101", "5.56x46 mm", "FMJ", 957, "Minillas South Tower", 243.69, "Venus"),
Experimentaldata("ak-101", "5.56x46 mm", "HP", 947, "Minillas South Tower", 243.69, "Saturn"),
Experimentaldata("ak-101", "5.56x46 mm", "M856A1", 940, "Minillas South Tower", 243.69, "Saturn")

]

for data in myDataset:
    print("\n----------------------------------------------\n")
    Projectilefunction(data)

# projectilefuction("ak-101", "5.56x46 mm", "warmageddon", 910, "Minillas South Tower", "243.69", 9.81)

# Serialization
myOutputpath = Path(__file__).parents[0]
myOutputfilepath = os.path.join(myOutputpath, 'Projectile-Motion.json')

print(myOutputpath)

with open(myOutputpath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataset], outfile)

 # Deserialization
deserialize = open(myOutputfilepath)
experimentJson = json.load(deserialize)

for e in experimentJson:
    print("\n----------------------------------------------\n")
    Projectilefunction(Experimentaldata(**e))
# Projectilefunction(experimentalData)



