import base as archivo_base
from datetime import datetime
import time
import argparse

username = "collectorscp"
password = "CsPco11ecC0R3"
#ip = "10.31.121.142"
tiempo = 2
listaComandos = ["show ver brief"]
fecha = time.strftime("%d/%m/%Y")
now = datetime.now()

def ejecucion(ip):
    tunel = archivo_base.Conexion(username, password, ip)

    if tunel != None:
        hostname = archivo_base.Hostname(tunel)
        print(hostname + "-" + fecha.replace("/", "-")
                                + "_" + now.strftime("%H_%M_%S") + ".txt" )
        for comando in listaComandos:
            print("El comando a ejecutar: " + comando)
            output = archivo_base.mandarComando(comando, tiempo, tunel)
            print(output)
            print("*" * 100)
            print("\n")        
            archivo_base.guardarArchivo(hostname + "-" + fecha.replace("/", "-")
                                + "_" + now.strftime("%H_%M_%S") + ".txt" , output)
    
        print(archivo_base.Hostname(tunel))
        archivo_base.disconnect(tunel)


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', nargs='+', type=str)
    args = vars(parser.parse_args())

    for link in args['url']:        
        ejecucion(link)

if __name__ == '__main__':
    Main()







    
    



    
