### NO QUIERO VER CODIGO ESTATICO NI HARDCODED####
import requests


nuevaVaribale = 12

#hardcoding

def borrar(headers, url, urn, password, username):

    response = requests.delete(url + urn, headers=headers, auth=(username, password), verify=False)
    print(response)


def saludo(nombre, edad):
    print(nombre, edad)

def saludo2(nombre, edad):
    print(nombre, edad)

"""
4 patas
rechina
tiene un dibujo
madera
cafe
########
4 patas
es blanca
plastico
se dobla
##########
4 patas
solida



"""
