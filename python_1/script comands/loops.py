from netmiko import ConnectHandler
import datetime
import time
import re
import subprocess
import smtplib
import os
import sys

"""
ip = "sbx-iosxr-mgmt.cisco.com"
user = "admin"
password = "C1sco12345"
port = 8181
tunnel = None
"""
"""
ip = "172.18.87.85 "
user = "rafaelg2"
password = "7Vn9c15c0.."
port = 8181
tunnel = None
"""
"""
def conexion():
    try:
        net_connect = ConnectHandler(device_type='cisco_xr', ip=ip,
                                          username=user, password=password, timeout=20)
        return net_connect
    except Exception as e:
        print(str(e))
        sys.exit()
"""
dispositivo = {
    "ip": "sbx-iosxr-mgmt.cisco.com",
    "username": "admin",
    "password": "C1sco12345" ,
    "port": 8181,
    "timeout": 20,
    "device_type" : "cisco_xr", 
}

def conexion():
    try:
        net_connect = ConnectHandler(**dispositivo)
        return net_connect
    except Exception as e:
        print(str(e))
        sys.exit()


def ejecutarComando(tunnel, command):
    try:
        comando = tunnel.send_command(command, delay_factor=5)
        #print(comando)
        #print("*" * 100)
        #return command + "\n" + "*" * 100 + "\n" + comando
        return comando
    except Exception as e:
        print(str(e))
        pass


def desconectar():
    tunnel.disconnect()


def guardar(comando):
    with open("nombre", "a") as f:
        f.write(comando)


tunnel = conexion()

res = ejecutarComando(tunnel, "show ip int brief")

# lista.index("probando"))

strALista = res.split()
inicio = strALista.index("Vrf-Name") + 1 
incremento  = strALista[inicio:]
rango = incremento.index("default") + 1 



for x in range (inicio, len(res.split()), rango ):
    print("show interface " + strALista[x])
    

#print(res.split())
#print(range(indice2))
#print(res)
#print(indice2)


