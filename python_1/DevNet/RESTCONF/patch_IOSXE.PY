import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://ios-xe-mgmt-latest.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/router/eigrp"

payload = """{
    "Cisco-IOS-XE-eigrp:eigrp": [
      {
        "id": 89,
        "eigrp": {
          "router-id": "3.3.3.6"
        },
        "network": [
          {
            "number": "0.0.0.0"
          }
        ] 
      }
    ]  
}"""


headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.patch( url, headers=headers, data = payload, verify=False)

print(response)
