import pandas as pd
df = pd.read_csv (r"C:\Users\14059\Desktop\Programming Learning\Python Tests\Byte Size Python\Solar System Facts\Distance_from_sun.csv")



def distance():
    planet_chosen = input('Hello, what planet would you like to know their distance from the Sun? \n')
    if planet_chosen == "Mercury":
        print(df['DISTANCE'][0],"Miles away from the sun")
    elif planet_chosen == "Venus":
        print(df['DISTANCE'][1],"Miles away from the sun")
    elif planet_chosen == "Earth":
        print(df['DISTANCE'][2],"Miles away from the sun")
    elif planet_chosen == "Mars":
        print(df['DISTANCE'][3],"Miles away from the sun")
    elif planet_chosen == "Jupiter":
        print(df['DISTANCE'][4],"Miles away from the sun")
    elif planet_chosen == "Saturn":
        print(df['DISTANCE'][5],"Miles away from the sun")
    elif planet_chosen == "Uranus":
        print(df['DISTANCE'][6],"Miles away from the sun")
    else:
        print(df['DISTANCE'][7],"Miles away from the sun")
    return


