
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:])


#Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for jugadores in players[:3]:
    print("Nombres de los finalistas:" , jugadores.title() )

#Copying a List
food = ["enchiladas", "mole", "pollo", "carnitas"]
wifefood = food[:]
food.append("moronga")
wifefood.append("nanches")

for comida in food[:]:
    print("Comida favorita de Rafael: " + comida)

for esposa in wifefood:
    print("Comida Favorita de esposa: " + esposa)

print("My Favorite food are: ")
print(food)

print("\n My wife´s food are: ")
print(wifefood)



