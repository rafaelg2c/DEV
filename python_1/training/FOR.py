"""
Carros = ["audi", "Nissan", "Ford"]
for cars in Carros:
    print("Marcas de carros: " + cars.title())
    print("Arpoveche el descuento\n")
    
print("Acude a tu sucursal más cercana!!")

for x in range(1,6):
    print(x)
"""
"""
squares = []


for value in range (1,11):
    square = value**2
    squares.append(square)
print(squares)


for value in range (1,11):
    squares.append(value**2)
print(squares)        

squares = [value**2 for value in range(1,11)]
print(squares)
"""


tercera = []

for valor in range(1,13):
    potencia = valor**3
    tercera.append(potencia)
print("Primera: " , tercera)    

#list Comprehension
potencias = [valor**3 for valor in range (1,13)]
print("Segundo: " , potencias)



