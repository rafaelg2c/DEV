import requests , json

url = "https://swapi.dev/api/people/8/"

payload = {}
headers = {}

#response = requests.request("GET", url, headers=headers, data = payload)

response2 = requests.get(url , headers=headers, data=payload).json()

data4 = json.dumps(response2, indent=2)

#data = (response.text.encode("UTF8"))

#json
#data2 = json.loads(data)#dict
#data3 = json.dumps(data2, indent=2, sort_keys=True)#str

#print(data3)
#print(data2)
#print(data)
print(data4)
