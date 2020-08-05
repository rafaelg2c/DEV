
personas = {
    "Liliana": ["inteligente", "bonita","amorosa"],
    "oliver": ["chistoso","pequeño","cacheton"],
    "Alma": ["mamona","creida","enojona"]
}

for nombre, ser in personas.items():
    print("\nCaracteristicas de :" + nombre + " son: " )
    for sere in ser:
        print("\t" + sere.title())

"""
#lista vacia
people = []

person = {
    "first name" : "rafael",
    "last name" : " garcia",
    "age" : 38,
    "city" : "cuernavaca"
    }
people.append(person)

person = {
    "first name" : "liliana",
    "last name" : " solis",
    "age" : 36,
    "city" : "cuernavaca"
    }
people.append(person)



for person in people:
    name = person["first name"].title() + person["last name"].title()
    city = person["city"].title()
    age = person["age"]
    print(name + " from " + city + " is " +  str(age) + " years old.")

"""