import xmltodict


archivo = open("user.xml","r")

xml = xmltodict.parse(archivo.read())


for e in xml["user"]["address"]:
    print(e)