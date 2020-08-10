from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

token = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
meraki = MerakiSdkClient(token)#constructor

orgs = meraki.organizations.get_organizations()

for org in orgs:
   if org["name"]== "DevNet Sandbox":
        org_id = org["id"]
        print(org_id)