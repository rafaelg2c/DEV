import base2 as archivo_base

username = "rafaelg2"
password = "7Vn9c15c0."
ip = "172.18.120.132"
tiempo = 2
listaComandos = ["show run | in router ospf", ""]

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
    