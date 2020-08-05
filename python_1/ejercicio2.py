import requests
from base_rest import borrar



username = "developer"
password = "C1sco12345"
url = "https://ios-xe-mgmt-latest.cisco.com:9443"
headers = {"Accept": "application/yang-data+json",
            "Content-type":"application/yang-data+json"}



urn = "/restconf/data/Cisco-IOS-XE-native:native/router/eigrp=189"

borrar(headers, url, urn, password, username)

#saludo("nombre", 12)

#<Response [204]>

