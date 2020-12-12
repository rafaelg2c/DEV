import requests
import json
from pprint import pprint

user = "admin"
passw = "Admin_1234!"


url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/svi-[vlan100].json"
myheader = {"Accept" :"Application/json"}
payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show run int vla 200",
    "output_format": "json"
  }
}                              #formato json
response = requests.post(url, data=json.dumps(payload), auth=(user, passw), headers=myheader, verify=False).json()
#print(response)

###########################   LOGIN NX-API REST #############################

auth_url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"
auth_data = {"aaaUser": {"attributes": {
    "name": user ,"pwd": passw}}}

auth_response = requests.post(auth_url, data=json.dumps(auth_data), timeout=5 , verify=False).json()
token = auth_response["imdata"][0]["aaaLogin"]["attributes"]["token"]
cookies = {}
cookies["APIC-cookie"]=token
print(cookies)

r = requests.post(url, headers=myheader, cookies=cookies, verify=False)
print(json.dumps(r.json(), indent=2 , sort_keys=True))