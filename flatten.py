import json
import pandas as pd

filePath = 'finalCars.json'

with open(filePath, 'r') as file:
	jsonData = json.load(file)

flattenedJson = []

for key, details in jsonData["911 GT2 RS's"].items():
	chassis, date = eval(key) 
	
	row = {
		"Chassis": chassis,
		"Date": date,
		"Model Name": details.get("modelName", ""),
		"Price": details.get("price", ""),
		"Result": details.get("result", ""),
		"Tags": ", ".join(details.get("tags", [])),
		"Seller Name": details.get("seller name", ""),
		"Location": details.get("location", ""),
		"Listing Details": "; ".join(details.get("listing details", [])),
		"year": details.get("year", "")
	}
	flattenedJson.append(row)

df = pd.DataFrame(flattenedJson)

outputFile = 'soldGT2.xlsx'
df.to_excel(outputFile, index = False, sheet_name = 'GT2 RS Data')

