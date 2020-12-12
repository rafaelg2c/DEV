import xml.etree.ElementTree as ET

archivo = open("user.xml","r")

xml = ET.parse(archivo)
root = xml.getroot()

for e in root:
    print(ET.tostring(e))

    print(xml)
    print(e.get("id"))

    






