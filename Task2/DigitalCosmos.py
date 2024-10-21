
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

    for planet in planets:
        if planet ['isPlanet']:
            name = planet['englishName']
            #mass = planet['mass'] 
            data = name.split()
            print(data)
        
fetch_planets()

def find_heaviest_planet(planets):
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet ['isPlanet']:
            name = planet['englishName']
            mass = 'massValue:',planet['mass']['massValue']
    
    #highest_mass = max(mass)
    print(f"The heaviest planet is {name} with a mass of {mass} kg.")

planets = fetch_planets()
find_heaviest_planet(planets)