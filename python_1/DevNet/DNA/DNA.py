import requests
import json

from requests.models import Response

#### GET token ####

url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

user = "dnacdev"
password = "D3v93T@wK!"

header = {"Coontent-type":"apllication/json"}

response = requests.post (url, headers=header, auth=(user, password)).json()
#print(response)
token = response["Token"]
#print(token)

##### GET CLIENTS HEALTH ####

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health"

query = {"timestamp":""}
header = {
    "x-auth-token": token
}

response = requests.get(url, headers=header, params=query).json()
# print(response)
# json = json.dumps(response, indent=2, sort_keys=True)
# #print(json)

print(f"clientes: {response['response'][0]['scoreDetail'][0]['clientCount']}")

scores = response["response"][0]["scoreDetail"]
#print(score)
for score in scores:
    if score["scoreCategory"]["value"] == "WIRED":
        print(f"Wired Cliente:{score['clientCount']}")
        score_values = score["scoreList"]
        for score_value in score_values:
            print(f"  {score_value['scoreCategory']['value']} : {score_value['clientCount']}")
    elif score["scoreCategory"]["value"] == "WIRELESS" :
        print(f" Wireless clientes: {score['clientCount']}")
        score_values = score["scoreList"]
        for score_value in score_values:
            print(f"  {score_value['scoreCategory']['value']} : {score_value['clientCount']}")
