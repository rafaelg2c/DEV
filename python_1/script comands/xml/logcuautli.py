import xmltodict , json


archivo = open ("LogCuautitlan.xml","r")
o = xmltodict.parse(archivo.read())

strJson = json.dumps(o , indent = 2 , sort_keys=True)

print(strJson)