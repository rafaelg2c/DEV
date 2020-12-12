import xmltodict, json

archivo = open("LogCuautitlan.xml", "r")

o = xmltodict.parse(archivo.read())

strJson = json.dumps(o, indent=2, sort_keys=True)
print(strJson)
"""
varJson = json.loads(strJson)


for x in range(0, 341304):
    try:

        print(varJson["results"]["result"][x]["field"][4]["v"]["#text"])

    except:
        pass


"""