import csv
import json

csvFilePath = 'text.csv'
jsonFilePath = 'text.csv'

data = {}

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        data[id] = rows
        id = rows['id']

with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))

