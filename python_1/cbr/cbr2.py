###CODED BY OSCAR SALGADO ORTIZ - OSCSALGA###
## SCRIPT TO MONITO nV IRL LINKS ##

import Base as db
from netmiko import redispatch
import smtplib
import sys
import time
import datetime


now = datetime.datetime.now()
horaActual = now.hour

archivo = "playalist"
comando = ["show log | i kernel: EXT2-fs", "show file systems", "show harddisk: filesys", "show harddisk:", "show stby-harddisk: filesys", "show stby-harddisk:", "show event manager statistics server"]
pivote = "200.79.231.233"

device1 = {
'ip': pivote 
}

emails = ["oscsalga@cisco.com"]
valores = ['4', '4', '4', '4', '4', '4', '4', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6']

def correo(personas, hostname, output):
    SUBJECT = "Problemas con el NV: " + hostname
    TEXT = "PROBLEMAS CON EL NV\n{}".format(output)
    gmail_sender = 'ciscomonitoreo@gmail.com'
    gmail_passwd = 'Devilmaycry2'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)
    try:

        for p in personas:
            receiver = p
            BODY = '\r'.join(['To: %s' % receiver,
                              'From: %s' % gmail_sender,
                              'Subject: %s' % SUBJECT,
                              '', TEXT])
            server.sendmail(gmail_sender, [receiver], BODY)
            print('email sent')
    except:
        print('error sending mail')
    server.quit()

def comandos(comando):
    output = conexion.send_command(comando + "\n")
    return output



all_devices = [device1]  # list of devices
for a_device in all_devices:
    cont = 0
    output = ""
    lista = list()
    try:
        file1 = open(archivo, 'r') 
        for jump in file1:
            #print(jump.strip())
            conexion = db.Drops(a_device['ip'])
            time.sleep(2)
            hostname = conexion.findHostname().replace("#", "")
            time.sleep(4)
            conexion = conexion.salto(jump + "\n")
            redispatch(conexion, device_type='cisco_xe')
            hostname2 = conexion.find_prompt()
            time.sleep(2)
            print("*" * 32)
            print("*Pivote: " + hostname + "*")
            print("*" + hostname2 + "*")
            print("*" * 32)
            print("\n")
            for comm in comando:
                output = comandos(comm)
                with open(hostname2.replace("#", "").replace("/", "") + "--" + str(now).replace(":","").strip() + ".txt","a") as f:
                    f.write("\nComando: " + comm + "\n" + output)
                print("Comando: " + comm + "\n" + output)
            print("*" * 100)
            conexion.write_channel("exit\n")
            time.sleep(4) 
    except Exception as e:
        print(e)

