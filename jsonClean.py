import re
import json

file = 'products.json'

with open(file) as file:
    data = json.load(file)


# Extracting the year from each modelName using regular expressions
for car_id, car_info in data["911 GT2 RS's"].items():
    model_name = car_info["modelName"]
    year_match = re.search(r'\b\d{4}\b', model_name) 

    year = year_match.group()
    print(f"Car ID: {car_id}, Year: {year}")

    car_info["year"] = year

with open('carsCleaned.json', 'w+') as f:
    json.dump(data, f, indent=4)

    

