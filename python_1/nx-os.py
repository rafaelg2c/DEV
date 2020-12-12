import requests
import json

url = "https://sbx-nxos-mgmt.cisco.com/ins"
user = "admin"
password = "Admin_1234!"

headers = {"Content-type" : "application/json"}

jsonCommand = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ver",
    "output_format": "json"

    }
}

response = requests.post(url, data=json.dumps(jsonCommand),
                         headers=headers,
                         auth=(user, password),
                         verify=False).json()

print(response)
print(json.dumps(response, indent=2, sort_keys=True))