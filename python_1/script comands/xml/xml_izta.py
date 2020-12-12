import xmltodict, json

archivo = open ("iztapalapa_3.xml", "r")

xml = xmltodict.parse(archivo.read())

print(xml.text)
#json_format = json.dumps(xml, indent = 2 , sort_keys=True)

#print(json_format)
