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
        network_Id = network["id"]
        pprint(network_Id)
"""
vlans = meraki.vlans.get_network_vlans(network_Id)
pprint(vlans)
"""