equipments = {}

equipments_active = True

while equipments_active:
    equipos = input("\nWhat equipment do you like? ")
    number =  input("\nHow many equipments do you like? ")

    equipments [equipos] = number

    responds = input("Do you need something else? ")
    if responds == "no":
        equipments_active = False

for equipos , number in equipments.items():
    print("you like: " +  equipos.title() + " amount: " +  number)
    print("thanks for you purchase")



#eem = open()
