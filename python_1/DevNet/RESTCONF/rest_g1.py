from pprint import pprint
import requests
import json

router = {"host": "ios-xe-mgmt-latest.cisco.com", "port": "9443", "username": "developer", "password": "C1sco12345"}

header = {"Accept": "application/yang-data+json",
         "Content-Type": "application/yang-data+json",
         #'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
         }

url = "https://"+router["host"]+":"+router["port"]+"/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

response = requests.get(url , headers=header, auth=(router["username"] , router["password"]), verify=False)

#print(response) 

api_data = response.json()
print("*" * 50)
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
print("*" * 50)
if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == "if-state-up":
    print("Interface is up")