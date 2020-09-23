"""
alien_color = ["blue", "green"]

if "blue" in alien_color:
    print("You have a prize")
if "green" in alien_color:
    print("You are the second")
"""

alien_color = "blue"
point = 0

if "blue" in alien_color:
    point = 5
elif "yellow" in alien_color:
    point = 10
elif "red" in alien_color:
    point = 15
else:
    print("You don´t have points")

print("You earn: " + str(point) +".")

