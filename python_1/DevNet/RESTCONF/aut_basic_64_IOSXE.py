import requests

url = "https://ios-xe-mgmt-latest.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/router/eigrp"

payload = {}

headers = { "Accept": "application/yang-data+json",
            "Content-type": "aplication/yang-data+json",
            "Authorization": "Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU="}


response = requests.get(url, headers=headers, data=payload, verify=False)

print(response.ok)