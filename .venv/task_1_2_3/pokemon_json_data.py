import requests
import json

#Tasks 1 & 2

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

json_data = response.text

pikachu_data = json.loads(json_data)

print(pikachu_data['name'])
print(pikachu_data['abilities'])

#Task 3
pokemon_list = [] 

def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    
    try:
        response = requests.get(url)
        pokemons = response.json()
        

       
        name = pokemons.get("name", "No Name")
        abilities = pokemons.get("abilities")
        weight = pokemons.get("weight", "no weight")
        print(f'Name: {name} \n Abilities: {abilities} \n Weight: {weight}')
        pokemon_list.append(weight)
    

    except requests.exceptions.RequestException as e:
      print(f'An exception occurred {e}')

def calculate_average_weight(pokemon_list):
    average_weight =  sum(pokemon_list)/ len(pokemon_list)
    print(f'Average weight of these pokemon: {average_weight}')
     #average weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
for name in pokemon_names:
   fetch_pokemon_data(name)
  
calculate_average_weight(pokemon_list)