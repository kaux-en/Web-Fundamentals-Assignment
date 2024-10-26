
import requests
import json

#venv - web_fundamentals



pokemon_names = ["pikachu", "bulbasaur", "charmander"]

def fetch_pokemon_data(pokemon_name):
    api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(api_url)
    json_data = response.text

    pokemon_data = json.loads(json_data)
    return pokemon_data

def calculate_average_weight(pokemon_names):
    weights = []
    for pokemon_name in pokemon_names:
        pokemon_data = fetch_pokemon_data(pokemon_name)
        weights.append(pokemon_data["weight"])
    weight_average = sum(weights) / len(weights)
    return weight_average
   


pokemon_data = fetch_pokemon_data("pikachu")
print(pokemon_data["abilities"])

print(calculate_average_weight(pokemon_names))