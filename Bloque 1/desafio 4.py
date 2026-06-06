#Ejercicio 4:
print ("Solución para el desafío 4 de programación")
entrada = input ("Introduce una lista de números enteros separados por coma: ")
lista_texto = entrada.split(",")
cantidad_pares = 0
for texto in lista_texto:
    número = int (texto.strip())
    if número % 2 == 0:
        cantidad_pares = cantidad_pares + 1
print ("Cantidad de números pares:", cantidad_pares)