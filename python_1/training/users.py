users = ["Angel", "adMIN"]#greeting and list empty

current_users = ["liliana", "armando", "Jorge", "paty"]#Checking Usernames:
new_users = ["Liliana", "ARMANDO" , "LEO"]



#greeting and list empty
if users:
    for user in users:
        if user.title() == "Admin":
           print("Hello Admin, would you like to see a status report?" )
        elif user != "Admin":
           print("Hello: " + user + ": thank you for logging in again..")
else:
   print("We need to find some users!\n")

#Checking Usernames:
for new_user in new_users:
   if new_user.lower() in current_users:
      print("Sorry " + new_user + " you will need to enter a new username.")
   else:
      print("hi " + new_user + " the username is available")


#Ordinal Numbers:
numbers = list(range(1,10))

for numeros in numbers:
   if numeros == 1: 
      print("1st")
   elif numeros == 2:
      print("2nd")
   elif numeros == 3:
      print("3rd")
   else:
      print(str(numeros) + "th") 






