import xmltodict, json

archivo = open("iztapalapa_3.xml", "r")

o = xmltodict.parse(archivo.read())

strJson = json.dumps(o, indent=2, sort_keys=True)
varJson = json.loads(strJson)


for x in range(0, 341304):
    try:

        print(varJson["results"]["result"][x]["field"][4]["v"]["#text"])

    except:
        pass


