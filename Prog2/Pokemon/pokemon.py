import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")
if response.status_code == 200:
    bulbasaur_dict = response.json()
    print(bulbasaur_dict)
    print(json.dumps(bulbasaur_dict, indent=4))
    with open("bulbasaur.json", "w") as f:
        json.dump(bulbasaur_dict, f, indent=4)