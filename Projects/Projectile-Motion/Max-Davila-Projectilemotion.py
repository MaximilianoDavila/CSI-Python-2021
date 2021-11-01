# gun = 'ak-101'
# caliber = '5.56x45 mm'
# ammunition = 'Warmageddon'
# Velocity_ms = 910

# building = 'Minillas South Tower'
# buildingheight = 243.69

# gravity_Ms = 9.81

# import math



def projectilefuction(gun:str, caliber:str, ammunition:str, Velocity_ms:int, building:str, buildingheigt:int, gravity_Ms:int):
    time_s = math.sqrt((2 * buildingheight) / gravity_Ms)
    distance_m = (Velocity_ms * time_s)

    print(f"The gun selected for this experiment is {gun}. the caliber of {gun} is {caliber}, and the ammunition of the {gun} is {ammunition}. The spped of the a the ammunition is {Velocity_ms}.")
    print(f'the building that we are going to use is the {building} in sanjuan, and the height of the {building} is {buildingheight}.')
    print('This day we were lucky that there is no air resistance.')

projectilefuction("ak-101", "5.56x46 mm", "warmageddon", 910, "Minillas South Tower", "243.69", 9.81)

