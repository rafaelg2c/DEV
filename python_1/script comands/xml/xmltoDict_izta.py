import xmltodict, json
from os import path

def logs(archivoXml):
    if path.exists(archivoXml):
        archivo = open(archivoXml, "r")
        count = len(open(archivoXml).readlines())
        o = xmltodict.parse(archivo.read())
        
        #print(o["searchWrapper"]["results"]["result"][1]["field"][0]["v"]["#text"])


        for cont in range(0, count):
            try:
                print(o["searchWrapper"]["results"]["result"][cont]["field"][0]["v"]["#text"])
            except:
                pass
    else:
        print("File Not Found")


if __name__== "__main__":
    logs("iztapalapa_3.xml")


"""
arhivo = open ("iztapalapa_3.xml", "r")
o = xmltodict.parse(arhivo.read()) #formato json
json_format = json.dumps(o, indent=2 , sort_keys=True)
varJson = json.loads(json_format)

print(json_format)
"""

     



