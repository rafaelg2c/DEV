import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


##### GET TOKEN- POST #####
url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "ciscopsdt"
        }
    }
}

headers = {
    "Content-type": "application/json"
}

response = requests.post(url, json.dumps(payload), headers=headers, verify=False).json()
#print(json.dumps(response, indent=2 , sort_keys=True))

token = response["imdata"][0]["aaaLogin"]["attributes"]["token"]
#print(token)

cookie = {}
cookie["APIC-cookie"] = token
#print(cookie)

######### GET APPLICATION PROFILE ############

url = "https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

payload = {}

headers = {"cache-control": "no-cache"}

response = requests.get (url , headers=headers, data=payload, cookies=cookie, verify=False).json()
#print(json.dumps(response, indent=2 , sort_keys=True))


######  MODIFY DECRIPTION ######
url  = "https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

payload_data =  {
     "fvAp": {
        "attributes": {
            "descr": "",
            "dn": "uni/tn-Heroes/ap-Save_The_Planet"
        }
     }
 }    

post_response = requests.post (url, data=json.dumps(payload_data), cookies=cookie, verify=False).json()
#print(post_response)

get_response = requests.get (url, headers=headers, data=payload, cookies=cookie, verify=False).json()
print(json.dumps(get_response, indent=2, sort_keys=True))