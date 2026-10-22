#Desafío 91

import random

temperaturas = []

# Generar 10 temperaturas aleatorias
for i in range(10):
    temperatura = random.uniform(-10.0, 40.0)
    temperaturas.append(temperatura)

# Mostrar las temperaturas generadas
print("Temperaturas generadas:")

for temperatura in temperaturas:
    print(round(temperatura, 2), "°C")

# Mostrar la lista completa
print("Lista de temperaturas:", temperaturas)
