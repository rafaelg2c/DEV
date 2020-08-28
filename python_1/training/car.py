
hombre = 23
hombre1 = 10
hombre2 = 87

car = "ford"

equipos = ["red", "cmts", "router", "sw"]

capa2 = "sw"
cable = "red" 


if capa2 and cable in equipos:
    print("Se tiene en bodega: " + capa2 + " y " + cable + ".\n")
else:
    print("realizar pedido")  
    print("\n")

  
cosa = [ "aretes", "mesa", "silla"]
cosas = "aretes"

if cosas in cosa:
    print("si esta " + cosas + "\n")
else:
    print("no\n")

if car == "ford":
    print("es verdad  " +  car.upper())
    print("\n")

print("is hombre == 23")
print(hombre  == 23)

print("is hombre == 10")
print(hombre1 == 10)

print("is hombre == 87")
print(hombre2 >= 89)
 