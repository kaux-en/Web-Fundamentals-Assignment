
import requests
import json

#venv - web_fundamentals



pokemon_names = ["pikachu", "bulbasaur", "charmander"]

def fetch_pokemon_data(pokemon_name):
    api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(api_url)
    json_data = response.text

    pokemon = json.loads(json_data)
    print(f"{pokemon["abilities"]}")

def calculate_average_weight(pokemon_list):
    api_url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(api_url)
    json_data = response.text

    pokemon = json.loads(json_data)
    average = (pokemon["weight"] / 3)
    print(average)


fetch_pokemon_data("pikachu")
fetch_pokemon_data("bulbasaur")
fetch_pokemon_data("charmander")

calculate_average_weight(pokemon_names)