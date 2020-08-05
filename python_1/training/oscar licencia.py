from random import randrange

nombre2 = None

def licencia(datosLista):
    global nombre2
    print("nombre: " + nombre)
    print("edad: " + edad)
    print("Nacionalidad: " + Nacionalidad)


    if Nacionalidad == "Mex" and calificacion > 8:
        print("licencia: " + nombre + Nacionalidad + str(randrange(1, 10000)))
        nombre2 = nombre
        return (True)

    elif not Nacionalidad == "Mex" and calificacion > 8:
        print("otorgar Licencia con registro CVEXT" + str(randrange(1,10000)))
        nombre2 = nombre
        return (True)
    else:
        print("no licencia")
        return (False)


def Agencia(licencia):
    if licencia == True:
        print("continuar proceso")
        #print(nombre2)
    else:
        print("no continuar")


licencia1 = licencia(["Rafael", "29", "Mex", 9])
Agencia(licencia1)

licencia2 = licencia("El flemas", "38", "usa", 9)
Agencia(licencia2)

"""
licencia3 = licencia("Monico", "38", "irl", 9)
Agencia(licencia3)
"""
