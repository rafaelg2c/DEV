from ncclient import manager
import xml.dom.minidom
import xmltodict
from pprint import pprint


equipo = {"host": "ios-xe-mgmt-latest.cisco.com", "port": "10000",
 "username": "developer", "password": "C1sco12345" }


netconf_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet2</name>
        </interface>
    </interfaces>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet2</name>
        </interface>
    </interfaces-state>
</filter>

"""


with manager.connect(host=equipo["host"], port=equipo["port"], username=equipo["username"], password=equipo["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' *58)
        print(capability)

        interface_netconf = m.get(netconf_filter)
        xmldom = xml.dom.minidom.parseString(str(interface_netconf))
        print(xmldom.toprettyxml(indent= "  "))
        print("*" *25 + "Break" + "*" *50)


        interface_python = xmltodict.parse(interface_netconf.xml)[
            "rpc-reply"]["data"]       
        pprint(interface_python)
        name = interface_python["interfaces"]["interface"]["name"]["#text"]  
        print(name)


     
        config = interface_python["interfaces"]["interface"]
        op_state = interface_python["interfaces-state"]["interface"] 

        print("start")
        print("Name:" + config['name']["#text"])
        print("description:" + config["description"])
        print("Packets In:" + op_state["statistics"]["in-unicast-pkts"])
        m.close_session()


