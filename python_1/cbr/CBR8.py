import base2 as archivo_base
from datetime import datetime
import time
import argparse

username = "oscsalgado"
password = "devilmycry2"
#ip = "10.31.121.142"
tiempo = 2
listaComandos = ["Term len 0","show log | i kernel: EXT2-fs","Sshow file systems","show harddisk: filesys", "show harddisk:", "show stby-harddisk: filesys", "show stby-harddisk:", "show event manager statistics server"]
fecha = time.strftime("%d_%m_%Y")
now = datetime.now()

def ejecucion(ip):

    
    tunel = archivo_base.Conexion(username, password, ip)

    if tunel != None:
        hostname = archivo_base.Hostname(tunel)
        print(hostname)
        
        archivo = hostname + "-" + fecha + "_" + now.strftime("%H_%M_%S") + ".txt"
                                
    
        for comando in listaComandos:
            print("El comando a ejecutar: " + comando)
            output = archivo_base.mandarComando(comando,tiempo, tunel)
            print(output)
            print("*" * 100)
            print("\n")       
            archivo_base.guardarArchivo(archivo, "\n" + hostname+"#"+ " " + comando + output)
    
    
        archivo_base.disconnect(tunel)


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', nargs='+', type=str)
    args = vars(parser.parse_args())

    for link in args['url']:        
        ejecucion(link)

if __name__ == '__main__':
    Main()




    #cat command.list | xargs -P 4 -I {} sh -c "echo {}; python3.4 principal.py {} "
    
    #,"show log","show pim vrf Mcast neigh","show pim vrf Mcast int","show pim vrf Mcast topo","show pim vrf Mcast mdt cache detail","show mrib vrf Mcast route detail","show mpls mldp database","show pim trace error interface mdt mldp mrib protocol rib rp rpf rpf-redirect stats