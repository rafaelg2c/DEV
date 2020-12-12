import yaml,json
from yaml import load , load_all


stream = open ('user.yaml', 'r')
documents = load_all(stream, Loader=yaml.FullLoader)
#print(documents)


#json_data2 = json.dumps(stream)
#json_data = json.loads(json_data2)

for doc in documents:    
    print(doc)


