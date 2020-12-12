ticket =  "How old are you? "
ticket += "\nEnter quit to exit "



while True:
    edad = input(ticket)
    if edad == "":
        continue
    if edad == "quit":
        break

    edad =int(edad)
    if edad < 4: 
       print("The ticket is free.\n")
    elif edad < 13:
        print("The ticket is $10.\n")
    else:
        print("The ticket is $15.\n")
    



