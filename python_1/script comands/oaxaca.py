import rds_base as archivo_base

username = "collectorscp"
password = "CsPco11ecC0R3"
ip = "10.99.7.6"
tiempo = 2
listaComandos = ["show ver", "show ip int bri", "show platf"]

tunel = archivo_base.Conexion(username, password, ip)

if tunel != None:
    for comando in listaComandos:
        print("El comando a ejecutar: " + comando)
        Archivo_comando = archivo_base.mandarComando(comando, tiempo, tunel)
        print(Archivo_comando)
        print("*" * 100)
        print("\n")        
        archivo_base.guardarArchivo("output.txt" , Archivo_comando)

    archivo_base.disconnect(tunel)



    