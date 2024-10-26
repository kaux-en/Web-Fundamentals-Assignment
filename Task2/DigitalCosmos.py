
#venv - space_api

import requests
import json


def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']


    for planet in planets:
        if planet ['isPlanet']:
            name = planet['englishName']
            mass = 'massValue:',planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

def fetch_planets():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    return planets
  


def find_heaviest_planet(planets):
    planets_mass = []
    for planet in planets:
        if planet ['isPlanet']:
            name = planet['englishName']
            mass_value = planet['mass']['massValue']
            planets_mass.append({"name": name, "mass_value": mass_value})
    
    heaviest_planet = max(planets_mass, key=lambda planet: planet["mass_value"])
    return heaviest_planet

planets = fetch_planets()
heaviest_planet = find_heaviest_planet(planets)
print(f"The heaviest planet is {heaviest_planet["name"]} with a mass of {heaviest_planet["mass_value"]} kg.")
