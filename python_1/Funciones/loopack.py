import random

num = random.randint(1,30)

listado = []


def interfaces(listado , num1 , num2 ):
    for num in range(num1, num2):
        listado.append("show interface loopback " + str(num))
    return listado

for x in interfaces(listado , 0 , num):
    print(x)
    
   










