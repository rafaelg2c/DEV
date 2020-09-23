from ncclient import manager
from pprint import pprint
import xmltodict
import json

router = {"ip" : "ios-xe-mgmt-latest.cisco.com",
"port": "10000", "username": "developer", "password": "C1sco12345"}

netconf_filter =""" 
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet2</name>
        </interface>
    </interfaces>
</filter>
"""

m = manager.connect(host=router["ip"],
                port=router["port"] , 
               username=router["username"],
               password=router["password"] , 
               hostkey_verify=False)

interface_netconf = m.get_config('running',netconf_filter)
# pprint(interface_netconf.xml)
# o = xmltodict.parse(interface_netconf)
#print(o)

# interface_netconf2 = xmltodict.parse(interface_netconf.xml)
# pprint(interface_netconf2)
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
pprint(interface_python["interfaces"]["interface"]["name"]["#text"])

m.close_session()