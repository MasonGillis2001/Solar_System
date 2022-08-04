import sys
sys.path.insert(0, 'Modules')
import Planets
import DistanceFromSun
import funfacts




def choices():
    #NEED TO MAKE IT NOT CASE SENSATIVE
    choice = input("What would you like to know about our solar system? \n [1] Age on a different planet \n [2] Distances from the Sun  \n [3] Random fact about our solar system \n" \
        " [4] For energy produced by the sun in seconds \n")

    if choice == ('1'):
        selection = input('What planet would you like to see your age on? ')
        age_on_planet(selection)
        return 
    elif choice == ('2'):
        DistanceFromSun.distance()
        return
    elif choice == ('3'):
        funfacts.fun_fact()
        return
    elif choice == ('4'):
        energy_produced()
        return



def age_on_planet(planet):
    age = int(input('How old are you? '))
    new_age = (age * Planets.EARTH_DAYS) / Planets.planets[planet]["length of year"]
    new_age2 = round(new_age)
    return print(new_age2) #round returns that value as a whole number

def energy_produced():
    sun_energy = 38
    time_seconds = int(input("Input in seconds, an amount of time and see how much energy the sun produced in that time. "))
    energy = sun_energy * time_seconds
    print(energy, 'Octillion joules')
    return

choices()



