from base_rest import borra2
import requests

url = "https://ios-xe-mgmt-latest.cisco.com:9443"
payload = {}
headers = {"Accept": "application/yang-data+json",
            "Content-type": "application/yang-data+json",
            "Authorization": "Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU="}
            
urn = "/restconf/data/Cisco-IOS-XE-native:native/router/eigrp=89"

#<Response [204]>

borra2(url, urn, headers, payload)