import json
databaseCompanies = []; 
jsonFile = open("databaseStored.json", "w")
with open('reached-out.txt') as f:
	for line in f:
		editedLine = line.strip().lower().split();	
		joined = ''.join(editedLine)
		databaseCompanies.append(joined)
json.dump(databaseCompanies, jsonFile, indent=2)
