# Desafío 14: Contador de palabras
# Programa que cuenta la cantidad de palabras en un texto ingresado por el usuario.

import string

def contar_palabras(texto):
    """
    Recibe un texto, elimina signos de puntuación
    y cuenta la cantidad de palabras.
    """
    # Eliminar signos de puntuación
    for signo in string.punctuation:
        texto = texto.replace(signo, "")

    # Separar el texto en palabras
    palabras = texto.split()

    # Contar palabras
    return len(palabras)


def main():
    texto = input("Ingrese un texto para contar sus palabras: ")

    if texto.strip() == "":
        print("No ingresaste ningún texto. La cantidad de palabras es 0.")
    else:
        cantidad = contar_palabras(texto)

        print("Resultado del análisis:")
        print("Texto ingresado:", texto)
        print("Cantidad total de palabras:", cantidad)


main()