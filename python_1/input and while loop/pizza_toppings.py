prompts = "What toppings do you want in your pizza: "
prompts += "\nEnter 'quit' when you finish. "


while prompts:
    toppings = input(prompts)
    if toppings == "quit":
         print("Thanks")
         break
    else:
        print("\nyou’ll add that topping to their pizza: " + toppings.title() + "\n")

