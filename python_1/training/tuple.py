
food = ("Arroz", "Pollo", "Chilaquiles", "Sopa", "Frijoles","tortillas")

food = ("Refresco", "Paella")

food = ("huevos","pollo","milanesa")

#modificar tuple
food = list(food)
food[0] = "arroz"
food[1] = "caldo de pollo"
food = tuple(food)


for foods in food:
    print(foods)

