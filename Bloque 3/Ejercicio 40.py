def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

resultado = mcd(numero1, numero2)

print("El MCD de", numero1, "y", numero2, "es:", resultado)
