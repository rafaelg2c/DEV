sandwich_orders = ["pastrami","Tornado", "jamoqueso", "pastrami", "sabores", "carnes", "pastrami"]

finished_sandwiches = []

print("We don't have pastrami")
while "pastrami" in sandwich_orders:
     sandwich_orders.remove("pastrami")
     
print("\n")
while sandwich_orders:
     current_sandwich = sandwich_orders.pop()
     print("I am working in your " + current_sandwich + " sandwich.")
     finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
      print("I made a " + sandwich + " sandwich.")

