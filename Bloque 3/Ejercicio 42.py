def invertir_palabras(texto, indice=0):
    palabras = texto.split()

    # Caso base
    if indice >= len(palabras):
        return ""

    # Caso recursivo
    resto = invertir_palabras(texto, indice + 1)

    if resto == "":
        return palabras[indice]
    else:
        return resto + " " + palabras[indice]


oracion = input("Ingrese una oración: ")

resultado = invertir_palabras(oracion)

print("Oración invertida:", resultado)
