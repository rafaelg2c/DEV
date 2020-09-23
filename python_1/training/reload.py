import rds_base as archivo_base

username = "rafaelg2"
password = "7Vn9c15c0."
ip = "172.18.120.132"
tiempo = 2
listaComandos = ["show platf | in CPU | ex RP | u cut -d ' ' -f1"]

tunel = archivo_base.Conexion(username, password, ip)

if tunel != None:
    for comando in listaComandos:
        print("El comando a ejecutar: " + comando)
        Archivo_comando = archivo_base.mandarComando(comando, tiempo, tunel)
        Archivo_comando = Archivo_comando[29:]
        #print("hw-module location " + Archivo_comando + " reload")
        lista = Archivo_comando.split()
        print(lista)  

        for tarjeta in lista:
            print("hw-module location " + tarjeta + " reload")

        
 #       for x in Archivo_comando:
#          print("hw-module location" + x + "reload")
 ##   print("*" * 100))
 #   print("\n")        
 #       archivo_base.guardarArchivo("output.txt" , Archivo_comando)
    archivo_base.disconnect(tunel)
#hw-module location reload