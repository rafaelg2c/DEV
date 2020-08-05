from netmiko import ConnectHandler

tipo = "cisco_xr"
username = "rafaelg2"
password = "7Vn9C15c020@1"
ip = "172.18.120.132"
command1 = "show ver"
command2 = "show ipv4 int bri"
command3 = "show platf"
archivo = "resultado1.txt"
file2 = "output.txt"

#FUNCION QUE CREA LA CONEXION SSH
def Conexion(ip):
    conexion = ConnectHandler(device_type=tipo, ip=ip,
                                         username=username, password=password, timeout=20)
    return conexion #REGRESA EL "TUNEL"

#FUNCION QUE EJECUTA UN COMANDO
def mandarComando(comando, tiempo):
    com = Conexion(ip).send_command(comando, delay_factor=tiempo)
    return com #REGRESA EL OUTPUT DEL COMANDO


resultado1 = mandarComando(command1, 2)
resultado2 = mandarComando(command2, 2)
resultado5 = mandarComando("show diag", 2)

print(resultado1)
print(resultado2)


#def guardar(archivo, resultado):
#    with open(archivo, "a") as f:
#        f.write(str(resultado))
# def NOMBREDELAFUNCION(ARGUMENTOS):

# FUNCION QUE GUARDA UN ARCHIVO
def guardar(archivo, resultado):
    with open(archivo, "a") as f:
        f.write(str(resultado))
    

#llamar funcion: NOMBREDELAFUNCION(ARGUMENTOS)
guardar(file2,resultado2)



guardar("diag.txt",resultado5)


#TERMINA EL TUNEL SSH
Conexion(ip).disconnect()


