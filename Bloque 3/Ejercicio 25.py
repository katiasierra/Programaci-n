# Desafío 25: Batalla Naval
# Importamos NumPy para trabajar con matrices

import numpy as np
import random

# Creamos el tablero de 5x5 lleno de ceros
tablero = np.zeros((5, 5), dtype=int)

# Colocamos 3 barcos en posiciones aleatorias
barcos_colocados = 0

while barcos_colocados < 3:
    x = random.randint(0, 4)
    y = random.randint(0, 4)

    # Verificamos que no haya un barco en esa posición
    if tablero[x][y] == 0:
        tablero[x][y] = 1
        barcos_colocados += 1

def disparar(x, y):
    """
    Verifica si en la posición indicada hay un barco o agua.
    Recibe las coordenadas x e y.
    """
    if tablero[x][y] == 1:
        print("¡Golpeaste un barco!")
    else:
        print("El disparo cayó al agua.")


def main():
    print("Bienvenido a Batalla Naval")
    print("El tablero es de 5x5.")
    print("Debes ingresar coordenadas entre 0 y 4.")

    # Pedimos coordenadas al usuario
    x = int(input("Ingrese la coordenada x: "))
    y = int(input("Ingrese la coordenada y: "))

    # Verificamos que las coordenadas sean válidas
    if 0 <= x <= 4 and 0 <= y <= 4:
        disparar(x, y)
    else:
        print("Coordenadas fuera del tablero.")
    # Mostramos el tablero para comprobar dónde estaban los barcos
    print("Tablero:")
    print(tablero)
main()