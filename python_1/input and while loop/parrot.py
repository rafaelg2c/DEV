"""
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != "quit":
    message = input(prompt)
    print(message)
    
    #if message != 'quit':
        #print(message)
"""

#flag, several events to end the program.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    if message == "run":
        active = False
    else:
         print(message)