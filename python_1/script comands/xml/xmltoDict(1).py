import xmltodict
from os import path


def logs(archivoXml):
    if path.exists(archivoXml):
        archivo = open(archivoXml, "r")
        count = len(open(archivoXml).readlines())
        o = xmltodict.parse(archivo.read())

        for cont in range(0, count):
            try:
                print(o["results"]["result"][cont]["field"][4]["v"]["#text"])
            except:
                pass
    else:
        print("File Not Found")


if __name__== "__main__":
    logs("LogCuautitlan.xml")
