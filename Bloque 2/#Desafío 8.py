#Desafío 8

# Desafío 8

numero = int(input("Ingrese un número entero: "))

divisores = [2, 3, 5, 7, 9, 10, 11]

for divisor in divisores:
    if numero % divisor == 0:
        print(f"El número {numero} es múltiplo de {divisor}.")
    else:
        print(f"El número {numero} NO es múltiplo de {divisor}.")
