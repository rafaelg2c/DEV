"""
Committed changes on ma0.test.bllab.it.bb.sky.com

RP/0/RP0/CPU0:ma0.test.bllab#conf t
Wed Apr  8 11:34:39.879 BST
Current Configuration Session  Line       User     Date                     Lock
00001000-00001ddc-00000b56     netconf    m.pressw Wed Apr  8 00:13:02 2020
00001000-00001ddc-00000b58     netconf    m.pressw Wed Apr  8 00:21:33 2020
RP/0/RP0/CPU0:ma0.test.bllab(config)#interface bundle-ether 9999
RP/0/RP0/CPU0:ma0.test.bllab(config-if)#shut
RP/0/RP0/CPU0:ma0.test.bllab(config-if)#root
RP/0/RP0/CPU0:ma0.test.bllab(config)#commit
Wed Apr  8 11:34:50.702 BST
RP/0/RP0/CPU0:ma0.test.bllab(config)#interface bundle-ether 9999.9999
RP/0/RP0/CPU0:ma0.test.bllab(config-subif)#no shut
RP/0/RP0/CPU0:ma0.test.bllab(config-subif)#root
RP/0/RP0/CPU0:ma0.test.bllab(config)#commit
Wed Apr  8 11:35:01.842 BST
RP/0/RP0/CPU0:ma0.test.bllab(config)


RP/0/RP0/CPU0:ma0.test.bllab#show configuration commit list
Wed Apr  8 11:54:02.924 BST
SNo. Label/ID              User      Line                Client      Time Stamp
~~~~ ~~~~~~~~              ~~~~      ~~~~                ~~~~~~      ~~~~~~~~~~
2    1000005304            m.presswa vty3:node0_RP0_CPU  CLI         Wed Apr  8 11:35:01 2020
3    1000005303            m.presswa vty3:node0_RP0_CPU  CLI         Wed Apr  8 11:34:50 2020

RP/0/RP0/CPU0:ma0.test.bllab#show configuration commit changes last 1
Wed Apr  8 11:38:04.493 BST
Building configuration...
!! IOS XR Configuration version = 6.5.3
interface Bundle-Ether9999.9999
!
end

RP/0/RP0/CPU0:ma0.test.bllab#show configuration commit changes last 2
Wed Apr  8 11:38:06.377 BST
Building configuration...
!! IOS XR Configuration version = 6.5.3
interface Bundle-Ether9999
 shutdown
!
interface Bundle-Ether9999.9999
!
end

RP/0/RP0/CPU0:ma0.test.bllab#show configuration rollback changes last 1
Wed Apr  8 11:38:11.830 BST
Building configuration...
!! IOS XR Configuration version = 6.5.3
no interface Bundle-Ether9999.9999
end

RP/0/RP0/CPU0:ma0.test.bllab#show configuration rollback changes last 2
Wed Apr  8 11:38:14.159 BST
Building configuration...
!! IOS XR Configuration version = 6.5.3
no interface Bundle-Ether9999
no interface Bundle-Ether9999.9999
end
"""

from lxml import etree
from ncclient import manager

root = etree.Element("roll-back-configuration", nsmap={None: "http://cisco.com/ns/yang/Cisco-IOS-XR-cfgmgr-rollback-act"})
etree.SubElement(root, "commit-id").text = "1000005303"

m = manager.connect(host="ma0.test.bllab.it.bb.sky.com", port=830, username="user", password="pass", device_params={"name": "iosxr"})
c = m.dispatch(root)
print(c.xml)
print(c.ok)
print(c.errors)

"""
RP/0/RP0/CPU0:ma0.test.bllab#show configuration commit list
Wed Apr  8 11:54:02.924 BST
SNo. Label/ID              User      Line                Client      Time Stamp
~~~~ ~~~~~~~~              ~~~~      ~~~~                ~~~~~~      ~~~~~~~~~~
1    1000005305            m.presswa netconf             YANG Frame  Wed Apr  8 11:53:50 2020
2    1000005304            m.presswa vty3:node0_RP0_CPU  CLI         Wed Apr  8 11:35:01 2020
3    1000005303            m.presswa vty3:node0_RP0_CPU  CLI         Wed Apr  8 11:34:50 2020

RP/0/RP0/CPU0:ma0.test.bllab#show configuration commit changes 1000005305
Wed Apr  8 11:54:10.278 BST
Building configuration...
!! IOS XR Configuration version = 6.5.3
no interface Bundle-Ether9999
no interface Bundle-Ether9999.9999
end
"""