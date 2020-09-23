import yaml
import json

with open ("yaml-data.yaml", "r") as data_yaml:
    data = yaml.safe_load(data_yaml)#Conver a YAML file to a Python dictionary.

#print(json.dumps(data,indent=2, sort_keys=True))

users = data["user"]
#print(data)
print(users["name"])
for role in users["roles"]:
    print(role)

users["location"]["city"] = "Dallas"

with open("yaml-data-edited.yaml", "w") as data_yaml:# save a YAML file from a PYTHON dictionary.
    yaml.safe_dump(data,data_yaml, default_flow_style=False)#
    
