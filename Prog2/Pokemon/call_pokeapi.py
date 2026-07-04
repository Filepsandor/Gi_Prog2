from pokeData import Pokemon
import json
import requests

def main():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")
    
    bulbasaur = Pokemon(**response.json())
    print(bulbasaur.stats)

if __name__ == '__main__':
    main()