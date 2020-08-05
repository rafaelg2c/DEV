number = {
    "rafael" : [7,8,19],
    "liliana" : [8,11,8],
    "patricia" : [7,8,19],
}


for person, numero in number.items():
    print(person + "´s favorite numbers are: " )
    for numeros in numero:
        print(" " + str(numeros))

print(number["liliana"][2])