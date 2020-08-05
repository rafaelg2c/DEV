rivers = {
    "china":"huang He",
    "rusia":"obi",
    "españa":"ebro",
    
}

for city,river in sorted(rivers.items()):
    print("The " + river.title() + ","+ " runs trough " + city.title() + ".")
print("\n")

for city in sorted(rivers.keys()):
    print(city.title())
print("\n")

for river in rivers.values():
    print(river.title())