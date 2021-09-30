planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
g_m2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

print("Calculate your weight in a different planet of uor Solar S")
myweight = int(input("what is your weight (pounds)? "))

myPlanet = input(f"Select a planet from the list: {planets}\n")
def calculateWeight(planet, mass):
    print("Earth mass in pound is: (mass)")

    w_kg = mass / 2.046
    print(f"Mass in kg: {w_kg}")

    n_lb = 4.45 

    planet_index = planets.index(planet)
    print(f"Your weight in {planets[planet_index]} is {(w_kg * g_m2[planet_index]) / n_lb} lb.")

calculateWeight(myPlanet, myweight)
