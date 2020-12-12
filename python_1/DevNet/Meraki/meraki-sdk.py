from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

token = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
meraki = MerakiSdkClient(token)#constructor

orgs = meraki.organizations.get_organizations()
#print(orgs)

for org in orgs:
    if org["name"]== "DevNet Sandbox":
        orgID = org["id"]
    #print(orgID)
    

params = {}
params['organization_id'] = orgID
networks = meraki.networks.get_organization_networks(params)
#pprint(networks)

for network in networks:
    if network["name"] == 'DevNet Sandbox ALWAYS ON':
        net_Id = network["id"]
        pprint(net_Id)

vlans = meraki.vlans.get_network_vlans(net_Id)
#pprint(vlans)

vlan = vlans[0]
vlan["name"] == "Python TEST-SDK"

update_vlan = {}
update_vlan["network_Id"] = net_Id
update_vlan["vlan_Id"] = vlan["Id"]
update_vlan["update_network_vlan"] = vlan

result = meraki.vlans.update_network_vlan(update_vlan)

result_vlan = meraki.vlans.update_network_vlan(net_Id)
pprint(result_vlan)



