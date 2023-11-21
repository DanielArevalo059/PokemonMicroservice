# PokemonMicroservice
 Communication Contract

 This microservice provides the name, type, species, description, and image hyperlink for a passed Pokemon ID. Nearly 900 Pokemon and pertinent data are stored in a JSON file provided <a href="https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/pokedex.json"> here</a>.

 <h3>Request Data</h3>
 To request the data, Pokedex_Microservice.py will continuously read the text file 'data_pipeline.txt' until a digit is entered in the file. The digit can be 1 - 898, although the microservice does not implement a catch for an out-of-range ID. A request in the file will look as simple as:

 5

  <h3>Receive Data</h3>
The same text file - 'data_pipeline.txt' - will then be replaced with the name, type, species, description, and image hyperlink to the corresponding Pokemon with a newline separating each piece of data. To continue the example above, after reading '5' in 'data_pipeline.txt', Pokedex_Microservice.py will replace '5' with the following data:

Name: Charmeleon
Type: ['Fire']
Species: Flame Pokémon
Description: Charmeleon mercilessly destroys its foes using its sharp claws. If it encounters a strong foe, it turns aggressive. In this excited state, the flame at the tip of its tail flares with a bluish white color.
Image: https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/hires/005.png
