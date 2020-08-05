lista = ["silla", "caja", "martillo", "cuchara", "anillo", "hoja"]
amigo = lista
yo = lista[:]

print("The first three items in the list are" , lista[0:3])
print("Three items from the middle of the list are:" , lista[2:4])
print("The last three items in the list are:" , lista[4:])

yo.append("guitarra")
print("Mis cosas son:" , yo)

amigo.append("Bateria")
print("Cosas de mi amigo" , amigo)

for me in yo:
    print("Mis cosas son:" , me)
print("\n")

for friend in amigo:
    print("Cosas de mi amigo" , friend)