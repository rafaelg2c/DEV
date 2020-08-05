import requests
import json

target = "https://sbx-nxos-mgmt.cisco.com/ins"
username = "admin"
password = "Admin_1234!"

header = {"content-type": "application/json"}

cmd = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": 
        "show ip interface brief",
    "output_format": "json"
  }
}

reponse = requests.post(target, 
                data=json.dumps(cmd),
                headers=header, 
                auth=(username,password),
                verify=False).json()

print(json.dumps(reponse, indent=2, sort_keys=True))

