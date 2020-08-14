
import requests
import base_rest 
import urllib3

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

equipo = base_rest.router
username = base_rest.username
password = base_rest.password

#print("\"oscar")

#uri ="Tu Nombre es : {}\nTu edad es: {}\nTu usrnames es: {}\n{}{}".format(edad, edad, username,password,nombre)
#uri = f"TuNombre es : {nombre}\nTuEdad: {edad}\n{password}\n{equipo}"


url = f'https://{equipo["host"]}:{equipo["port"]}'
#url = https://{}:{}'.format(equipo["host"], equipo["port"])
url2 = "/restconf/data/Cisco-IOS-XE-native:native/router/eigrp=189"
#print(url)
uri = f"{url}{url2}"
print(uri)

payload = {}
headers = {"Accept":"application/yang-data+json",
            "Content-type":"application/yang-data+json",
            "Authorization": "Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU="}

headers2 = {"Accept":"application/yang-data+json",
            "Content-type":"application/yang-data+json"}

#response = requests.delete(uri, headers=headers, data=payload, verify=False)
#response = requests.request("DELETE", uri, data=payload, headers=headers, verify=False)
response = requests.delete(uri, headers=headers2, auth=(username, password) , data=payload, verify=False)



#print(response.text.encode("utf8"))


