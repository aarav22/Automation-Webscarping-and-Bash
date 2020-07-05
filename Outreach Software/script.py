import json
import pandas as pd
import math

databaseCompanies = []; 

with open("databaseStored.json", "r") as jsonFile_0: 
	databaseCompanies = json.load(jsonFile_0)	
with open("names.json", "r") as jsonFile: 
	names = json.load(jsonFile)		 
with open("email.json", "r") as jsonFile_2: 
	emails = json.load(jsonFile_2)	
relevantData = pd.read_csv('relevant.csv', delimiter = ',', usecols = ['Company Name', 'Founders Email Ids'])
relevantNames = []
relevantEmails = []
for name, email in zip(relevantData['Company Name'], relevantData['Founders Email Ids']):
	partsName = name.strip().lower().split()
	nameJoined = ''.join(partsName) 
	if (nameJoined not in databaseCompanies):
			relevantNames.append(name) 
			relevantEmails.append(email)



data = pd.DataFrame(list(zip(relevantNames, relevantEmails)), columns=['Names', 'Emails'])
data.to_csv('FinalData.csv')
		 


