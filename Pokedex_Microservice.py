# Daniel Arevalo
# CS 361 Microservice project
import json
json_file = open("pokedex.json", "r")
pokedex = json.load(json_file)

def main():
    while True:
        with open('data_pipeline.txt', 'r', encoding='utf-8') as in_ID:
            id = in_ID.read()
            if id.isdigit():
                id = int(id)-1
                with open('data_pipeline.txt', 'w', encoding='utf-8') as out_data:
                    out_data.write('')
                    out_data.write(f"Name: {pokedex[id]['name']['english']}\n"
                      f"Type: {pokedex[id]['type']}\n"
                      f"Species: {pokedex[id]['species']}\n"
                      f"Description: {pokedex[id]['description']}\n"
                      f"Image: {pokedex[id]['image']['hires']}")
                    out_data.close()

main()