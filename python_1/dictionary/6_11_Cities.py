cities = {
    "tetela del volcan":{
        "country" : "méxico",
        "population" : 122916000,
        "volcano" : "Popocatépetl",
        },
    
    "Hengduan" : {
        "country" : "china",
        "population" : 1380996000,
        "volcano" : "Tengchong",
        },
    "Campania" : {
        "country" : "Italy",
        "population" : 60674000,
        "volcano" : "Volcán Solfatara",
        }
}
 
#print(cities)
for city, info in cities.items():
    country = info["country"].title()
    population = info["population"]
    volcano = info["volcano"].title()
    print("\n" + city.title() + " is in " + country)
    print("   has " + str(population) + " habitants")
    print("   the " + volcano + " is nearby")

    print(info["country"])
