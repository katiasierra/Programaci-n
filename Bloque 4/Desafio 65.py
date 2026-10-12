import math

class Figura:
    def area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


# Crear objetos
circulo = Circulo(5)
cuadrado = Cuadrado(4)

# Guardarlos en una misma lista
figuras = [circulo, cuadrado]

# Recorrer la lista
for figura in figuras:
    print("Figura:", type(figura).__name__)
    print("Área:", figura.area())
    print()
