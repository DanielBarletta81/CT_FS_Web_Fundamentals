import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    bodies = response.json()['bodies']
    planets = {"name": [], "mass": []}
    #process each planet info
    for planet in bodies:
        if planet['isPlanet']:
            name = planet.get('englishName')#get planet English name
            mass = planet.get('mass')#get planet mass
            orbit_period = planet.get('sideralOrbit')#get planet orbit period
            planets["name"].append(name)
            planets["mass"].append(mass['massValue'])
            
            print(f"\n Planet: {name},\n Mass: {mass['massValue']} kg ,\n Orbit Period: {orbit_period} days")
    print(planets)
    return planets           
            
def find_heaviest_planet(planets):
    combined_list = []
    name = planets['name']
    mass = planets['mass']
    heaviest = max(mass)
    for i in range(0,min(len(name),len(mass))):
        combined_list.append(name[i]+ " : " + str(mass[i]))
        
    print(combined_list)
    print(f"The heaviest planet is {name[i]} with a mass of {heaviest} kg.")
    return name[i], heaviest


    
#for key, val in planets.items():
 #       for i in key:
 #            print("{} : {}".format( i, val))
    
planets = fetch_planet_data()
find_heaviest_planet(planets)

