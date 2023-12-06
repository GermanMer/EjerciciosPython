#Exercise 4: Sort JSON keys in and write them into a file
#Sort following JSON data alphabetical order of keys

#sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

#Expected Output:
#{
#    "age": 29,
#    "id": 1,
#    "name": "value2"
#}

import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

with open("sampleJson.json", "w") as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)

# Cargar el objeto JSON desde el archivo
with open("sampleJson.json", "r") as read_file:
    data = json.load(read_file)

# Imprimir el objeto cargado con el formato deseado
print(json.dumps(data, indent=4, sort_keys=True))
