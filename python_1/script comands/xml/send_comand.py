from netmiko import ConnectHandler
import datetime
import time
import re
import subprocess
import smtplib
import os
import sys

dispositivo = {
    "ip": "sbx-iosxr-mgmt.cisco.com",
    "user": "admin",
    "password": "C1sco12345",
    "port": 8181,
    "timeout": 20
}
tunnel = None

def conexión():
    try:
        net_conect = ConnectHandler (**dispositivo)


        
        
        return net_conect
    except Exception as e:
        print(str(e))
        sys.exit()

def ejecutar_comando(tunnel,comando):
    try:
        comando = tunnel.send_comando(comando, delay_factor = 5)
        return comando
    except Exception as e:
        print(str(e))
        sys.exit()

def desconectar():
    tunnel.




    

       







  

    


