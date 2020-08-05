pets = []

canela = {
    "name" : "canela",
    "breed" : "french poodle",
    "own" : "rafael"
}
pets.append(canela)

bigotes = {
    "name" : "bigotes",
    "breed" : "mestizo",
    "own" : "rafael"
}
pets.append(bigotes)


for pet in pets:
    name = pet["name"].title()
    breed = pet["breed"].title()
    own = pet["own"].title()
    print("\n"+ name + "," + " breed " + breed + "," + " own " + own + ".")


  