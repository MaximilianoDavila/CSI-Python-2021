planet = ["Mercury", "Venus", "Earth", "Mars","Jupiter", "Saturn", "Uranus", "Neptune"]
rel_gravity = [2.65, 1.11, 2.64, 0.40, 0.94, 1.19, 0.88]

print("small step for space and a big step on other planets")
myjump = float(input("What is your jump's lenght on Earth(meter)? "))

myplanets = input(f"Select a planet from the list: {planet}")
def Calculatejump(planets, meter):
    print(f"your jump in Earth is: {meter}")

    planet_index = planet.index(planets)

    print(f"Your weight in {planet[planet_index]} is {(myjump * rel_gravity[planet_index])} meters.")

Calculatejump(myplanets, myjump)