
name = {
    "luz", "alma","lucy", "daniel"
}
 
name2 = ["daniel", "lucy"]

for poll in sorted(name):
    if poll in name2: 
        print(poll.title() + " Thanks for take your poll")
    else:
        print(poll.title() + " take your poll")   
 