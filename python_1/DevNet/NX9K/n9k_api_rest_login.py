import requests
from pprint import pprint
import json

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload = """ {"aaaUser": {"attributes": {
          "name": "admin","pwd": "Admin_1234!"}}}"""

headers = {
  'Content-Type': 'application/json',
   #'Cookie': 'nxapi_auth=dzqnf:zI4Z4knVbeW7Tzr7V63fYlqUkZE=; APIC-cookie=jaIcX8XYqzPRuoWwxoH6riSDKsjDB2HGyTlANfLnymRQD6JZkQA8qIrwIZx5JVGUIel3kKkJG0l4dNly3aubseBBCrV5/0LiqwFJ8ACtOWkGSf8Jy3QkVZ7e92uHN3+CAzJiIApT2iTVrAmz8vhhOTFTSt6pxsX+xHlb3mnrApo='
}

response = requests.post( url, headers=headers, data = payload, verify=False).json()
#response_data = json.dumps(response, indent=2 , sort_keys=True)
# #print(response_data)

token = response["imdata"][0]["aaaLogin"]["attributes"]["token"]
#pprint(token)

cookies = {}
cookies["APIC-cookie"]=token
pprint(cookies)


url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/svi-[vlan300].json"

#get
payload = {}
#conf
payload_conf = """{
    "sviIf": {
        "attributes": {
            "dn": "sys/intf/svi-[vlan300]",
            "descr": "PUT_REST_PYTHON"
        }
    }
}  """

headers = {
  #'Authorization': 'Bearer YC5/s4C1MSmWrjhj8Mn9EVHIO4tTjQg2KGli9weasUmos7Q5oqee6Izg7Lfn7PdnZmSC/39aMV+t9t7pFQ47FFfIeMs6SHRDr2y2Jv9EgbOu7bwHshljyedCVHzB3xGjF52TXRkr9B61fkHe17b/c4Mv94enq2EH0cFUs3rVs4M=',
  'Content-Type': 'application/json',
}

put_response = requests.get(url, headers=headers, cookies=cookies, data=payload, verify=False)#.json()
#print(put_response)

#sintaxis para postman
#put_response_2 = json.dumps(put_response, indent=2, sort_keys=True)
#print(put_response_2)
api_data = put_response.json()
print("########### descripción ##########")
pprint(api_data["imdata"][0]["sviIf"]["attributes"]["descr"])
print("########### state ##########")
if api_data["imdata"][0]["sviIf"]["attributes"]["adminSt"]=="down":
  print("Interfaz down se envia correo NOC")
#print(api_data)