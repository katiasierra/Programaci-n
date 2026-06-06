#Ejercicio 3:
print ("Solución para el desafio 3")
n = int(input("Ingrese un número entero positivo: "))
resultado = 0
for numero in range(1, n + 1):
    resultado = resultado + numero
print("La suma de los primeros", n, "números naturales es:", resultado)