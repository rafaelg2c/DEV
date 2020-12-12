from netmiko import ConnectHandler
import time

dispositivo = {
    "ip": "sbx-iosxr-mgmt.cisco.com",
    "username": "admin",
    "password": "C1sco12345" ,
    "port": 8181,
    "device_type" : "cisco_xr",
    "timeout" : 20
}
lista_comandos = ["show ip int brief", "sho ver" , "show run int Loop100"]

net_connect = ConnectHandler(**dispositivo)
#print(net_connect.find_prompt())
time.sleep(1)
for lista in lista_comandos:
    comando = net_connect.send_command(lista, delay_factor=2)
    
    print("Comando ejecutado " + comando)

    with open ("interface.txt","a") as F:
        F.write(comando)


net_connect.disconnect()




