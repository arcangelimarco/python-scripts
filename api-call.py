####################################################
################ Tutorial API Call #################
#https://www.dataquest.io/blog/python-api-tutorial/#
####################################################

import requests
import json


def jsonPrint(jsonObj):
    output = json.dumps(jsonObj, sort_keys=True, indent=2)
    print(output)

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
#print(response.json())
jsonOutput = response.json()
jsonPrint(jsonOutput)

people = jsonOutput['people']
passengers_names = []
for passengers in people:
    people_name = passengers['name']
    passengers_names.append(people_name)

print("\nPeople in IIS right now:\n")
print(passengers_names)