import json


file = 'carsCleaned.json'


with open(file) as f:
    data = json.load(f)

for key, value in data["911 GT2 RS's"].items():
    
    if "Porsche 935" in value["modelName"]:
        value["modelName"] = "Porsche 935"
    elif "Clubsport" in value["modelName"]:
        value["modelName"] = "Porsche 911 GT2 RS Clubsport"
    elif "GT2 RS" in value["modelName"]:
        value["modelName"] = "Porsche 991.2 GT2 RS"

with open('finalCars.json', 'w+') as f:
    json.dump(data, f, indent=4)
