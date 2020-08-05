prompts = "What toppings do you want in your pizza: "
prompts += "\nEnter 'quit' when you finish. "

active = True

while active:
    toppings = input(prompts)

    if toppings == "quit":
        break
    if toppings == "test":
        active = False
        print("Thanks")
    else:
        print("\nyou’ll add that topping to their pizza: " + toppings.title() + "\n")
        #active = True