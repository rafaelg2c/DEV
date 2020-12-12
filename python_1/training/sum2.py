# entero = 23
# flotante = 54.23
# cadena = "esto es una cadena"
# lista = ["valor", "lo que sea", 234, 2356.26]  esto es una lista con varios valores
# listaVacia = [] 

#lista = []
#print(lista)
#lista.append("aa")
#print(lista)

lista =[]
resultado = 0


for contador in range(1, 7):
    valores = input("introduce un numero: ")
    lista.append(int(valores))
print(lista)

for x in lista:
    print(x)
    resultado = resultado + x


print("\n")
print("*" * 50)
print("EL RESULTADO ES:" + str(resultado))
    





