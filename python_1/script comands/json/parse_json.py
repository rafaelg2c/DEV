import json


with open ('user.json','r') as user_json:
    data_json = json.load(user_json)
    #data2_json = json.dumps(data_json)

    #parse = json.parse(data_json)
    print(data_json["marcadores"][2])

#data_jason = json.load(open("user.json"))


