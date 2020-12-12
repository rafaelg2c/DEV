favorite_places = {}


favorite_places["Rafa:"] = "egipto" , "españa" , "escocia"

for rafa , place in favorite_places.items():
    print(rafa , "likes this places")
    for place in favorite_places.values():
        print(place)

print(type(favorite_places))





