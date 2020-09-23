from acitoolkit.acitoolkit import *

# See Capabilities
# dir()

url  = "https://sandboxapicdc.cisco.com"
user = "admin"
pw = "ciscopsdt"

# Create the session object
session = Session(url, user, pw)

# Login to the session
session.login()

# Get Tenants
# tenants = Tenant.get(session)
# for tenant in tenants:
#     print(tenant.name)
#     print(tenant.descr)
#     print('*' * 30)
#     print(' ')


# Create a new Tenant
new_tenant = Tenant("Python_test_RG")
#new_tenant.get_url()
#new_tenant.get_json()

# Create the application profile and the EPG
anp = AppProfile("RG_APP", new_tenant)
epg = EPG("RG_APP" , anp)

# Create de L3 Namespace
context = Context("RG_VRF", new_tenant)
bridge_domain = BridgeDomain("RG_BD", new_tenant)

#Associate the BD with the L3 Namespace
bridge_domain.add_context(context)
epg.add_bd(bridge_domain)

#### Tenant Creation is completed ###
print(new_tenant.get_url())
print(new_tenant.get_json())
# response = session.push_to_apic(
#     new_tenant.get_url(), data=new_tenant.get_json()) 
# print(response)

tenants = Tenant.get(session)
for tenant in tenants:
    if tenant.name == 'Python_test_RG':
        print(tenant.name)
    else:
        print(tenant.name)
        print(tenant.descr)
        print('*' * 30)
        print(" ")

new_tenant.mark_as_deleted()
response = session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())
print(response)



