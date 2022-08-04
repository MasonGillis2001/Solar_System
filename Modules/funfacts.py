import random

facts = ["You can't stand on Uranus", "The whole of Mars is as cold as the South Pole", \
"Saturn's rings are 90% water", "Jupiter's largest moon has a salty ocean that contains more water than on Earth", \
"Mercury takes roughly three Earth months to orbit the Sun", "It would take 100 times longer to travel around the Sun than the Earth", \
"A day is longer than a year on Venus", "Pluto isn't the only dwarf planet in our Solar System - we have six", "The Solar System is roughly 4.5 billion years old" \
"The Solar System might not end with Pluto","Mercury is shrinking.","A block of lead on Venus would melt like a block of ice on earth.", \
"Pluto probably wasn't named after Pluto the Disney character.","Two of Saturn's moon have water."]

def fun_fact():
    random_fact = random.choice(facts)
    print(random_fact)
    return

fun_fact()