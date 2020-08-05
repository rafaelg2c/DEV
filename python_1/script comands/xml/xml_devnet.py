import xml.dom.minidom
import xmltodict
import json

"""
xml1 =  open("item.xml" ,"r")
data = xml.dom.minidom.parseString(xml1)
data_xml = data.toprettyxml()
print(data_xml)
"""

xml1 = open ("item.xml", "r")
data = xmltodict.parse(xml1.read())

#print(data["item"]["a:table"]["@xmlns:a"])
#print(data["item"]["b:table"]["@xmlns:b"])
 

#formato json
#data_xml= json.dumps(data, indent=2 , sort_keys=True)
#print(data_xml)

data2 = data["item"]["a:table"]["@xmlns:a"]
data3 = json.dumps(data2)
print(data3)



