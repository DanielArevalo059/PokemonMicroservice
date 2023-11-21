# PokemonMicroservice

 This microservice provides the name, type, species, description, and image hyperlink for a passed Pokemon ID. Nearly 900 Pokemon and pertinent data are stored in a JSON file provided <a href="https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/pokedex.json"> here</a>.

 <h3>Request Data</h3>
 To request the data, Pokedex_Microservice.py will continuously read the text file 'data_pipeline.txt' until a digit is entered in the file. There are 898 Pokemon stored in the JSON file and the microservice will assume that the data is within range. A request in the file will look as simple as:

 5

  <h3>Receive Data</h3>
The same text file - 'data_pipeline.txt' - will then be replaced with the name, type, species, description, and image hyperlink to the corresponding Pokemon with a newline separating each set of data. To continue the example above, after reading '5' in 'data_pipeline.txt', Pokedex_Microservice.py will replace '5' with the following:


<p>Name: Charmeleon</p>
<p>Type: ['Fire']</p> 
<p>Species: Flame Pokémon</p>
<p>Description: Charmeleon mercilessly destroys its foes using its sharp claws. If it encounters a strong foe, it turns aggressive. In this excited state, the flame at the tip of its tail flares with a bluish white color.</p>
<p>Image: https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/hires/005.png</p>

<h3>UML</h3>
![PokemonMicroservice_UML ](https://github.com/DanielArevalo059/PokemonMicroservice/assets/114385405/97011fd1-c215-43b8-8106-7b29de99390d)
