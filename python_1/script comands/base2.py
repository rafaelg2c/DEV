from netmiko import ConnectHandler
import time


#CONEXION SSH
def Conexion(username, password, ip):
    
    try:
        tunel = ConnectHandler(device_type="cisco_xr", ip=ip,username=username, password=password, timeout=20)
        
        print("conexión establecida")
        return tunel                                   
    except Exception as error:
        print(str(error))
        print("Error en la conexión")
                                     

#EJECUTA UN COMANDO
def mandarComando(comando, tiempo , tunel):
    try:
        com = tunel.send_command(comando, delay_factor=tiempo)
        return com #REGRESA EL OUTPUT DEL COMANDO
    except Exception as error:
        print(str(error))
        print("error al mandar comando")

def Hostname(tunel):
    try:
        hostname = str(tunel.find_prompt()).split(':', 1)[-1].strip()
        time.sleep(2)
        hostname = hostname.replace("#", "")
        return hostname
    except Exception as error:
        print(str(error))
        print("error al encontrar el Hostanme")



def guardarArchivo(docto1, comando):
    with open(docto1, "a") as f:
        f.write(str(comando))


def disconnect(tunel):
    try:
        tunel.disconnect()
        print("Tunel terminado")
    except Exception as error:
        print(str(error))
        print("error al desconectar")
