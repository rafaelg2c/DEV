names = True

all_names = []



while names:
    name = input("Ingresa tu nombre o '0' para salir: ")
    all_names.append(name)
    if name == "0":
        names = False

print("The names are: ")    
for end in all_names: 
    print(end)
      

def info (name, age, address):
    print("Nombre: " + name)
    print("age: " + str(age))
    print("Address: " + address)

info("Rafael", "23", "maron2")

