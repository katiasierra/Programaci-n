# Desafío 32: Verificación y cálculo de números primos

def es_primo(numero):
    """
    Verifica si un número es primo.
    Devuelve True si es primo y False en caso contrario.
    """
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


def contar_primos(lista):
    """
    Cuenta cuántos números primos hay en una lista.
    Devuelve la cantidad de números primos encontrados.
    """
    contador = 0

    for numero in lista:
        if es_primo(numero):
            contador += 1

    return contador


def main():
    # Lista de ejemplo
    numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    print("Lista:", numeros)

    cantidad = contar_primos(numeros)

    print("Cantidad de números primos:", cantidad)

    print("\nVerificación individual:")
    for numero in numeros:
        if es_primo(numero):
            print(numero, "es primo")
        else:
            print(numero, "no es primo")
main()