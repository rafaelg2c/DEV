

def licencia(nombre, edad,  Nacionalidad, calificacion):
    print("nombre: " + nombre )
    print("edad: " + edad)
    print("Nacionalidad: "  + Nacionalidad)

    if Nacionalidad == "Mex" and calificacion > 8:
        print("licencia: " + nombre + Nacionalidad +"12389" )
        return ("si")
    elif not Nacionalidad == "Mex" and calificacion > 8:
        print("otorgar Licencia con registro CVEXT783738")
        return ("si")
    else:
        print("no licencia")
        return("no")

    
def Agencia(licencia):
    if licencia == "si":
        print("continuar proceso")
    else:
        print("no continuar")

licencia1 = licencia("Rafael","38","Mex", 10)
licencia2 = licencia("Angel","50","usa", 5)
licencia3 = licencia("hector","30","Bra", 9)

Agencia(licencia1)
Agencia(licencia2)
Agencia(licencia3)




