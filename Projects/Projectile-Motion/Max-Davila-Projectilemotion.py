import math
# gun = 'ak-101'
# caliber = '5.56x45 mm'
# ammunition = 'Warmageddon'
# Velocity_ms = 910

# building = 'Minillas South Tower'
# buildingheight = 243.69

# gravity_Ms = 9.81

# import math



def projectilefuction(experimentaldata: Experimentaldata):
    time_s = math.sqrt((2 * experimentaldata.buildingheight) / experimentaldata.gravity_Ms)
    distance_m = (experimentaldata.velocity_ms * time_s)

    print(f"The gun selected for this experiment is {experimentaldata.gun}. the caliber of {experimentaldata.gun} is {experimentaldata.caliber}, and the ammunition of the {experimentaldata.gun} is {experimentaldata.ammunition}. The spped of the a the ammunition is {Velocity_ms}.")
    print(f'the building that we are going to use is the {experimentaldata.building} in sanjuan, and the height of the {experimentaldata.building} is {experimentaldata.buildingheight}.')
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
ExperimentalData("ak-101", "5.56x46 mm", "warmageddon","MB556A1", 910, "Minillas South Tower", 243.69, 9.81),
ExperimentalData("ak-101", "5.56x46 mm", "warmageddon","MBSS", 910, "Minillas South Tower", 243.69, 9.81),
ExperimentalData("ak-101", "5.56x46 mm", "warmageddon","MB", 910, "Minillas South Tower", 243.69, 9.81),
ExperimentalData("ak-101", "5.56x46 mm", "warmageddon","MBSS", 910, "Minillas South Tower", 243.69, 9.81),

]
for data in myDataset:
    print("\n----------------------------------------------\n")
    projectilefunction(data)

# projectilefuction("ak-101", "5.56x46 mm", "warmageddon", 910, "Minillas South Tower", "243.69", 9.81)



