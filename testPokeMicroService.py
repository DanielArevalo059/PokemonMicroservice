

poke_id = input("Enter Pokemon ID: ")
with open('data_pipeline.txt', 'w', encoding='utf-8') as out_file:
    out_file.write("")
    out_file.write(poke_id)
