from graphviz import Digraph



favorite_places = {
    "rafael" : ["egipto" , "españa" , "escocia"],
    "liliana" : ["españa", "francia", "oaxaca"],
    "jorge" : ["cancun", "alemania", "cuba"]
    }

for name, place in favorite_places.items():
    print(name.title() + " likes this places")
    for places in place:
        print("\t" "-" + places.title())

print(favorite_places["rafael"][0])

