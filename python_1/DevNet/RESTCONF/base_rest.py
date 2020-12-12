### NO QUIERO VER CODIGO ESTATICO NI HARDCODED####
import requests

def borra2(url, urn, headers, payload):
        respuesta = requests.delete(url + urn, headers=headers, data=payload ,verify=False)
        print(respuesta.ok)
        print(respuesta.status_code)