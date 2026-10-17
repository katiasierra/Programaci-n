#Desafío 96

inventario = {}

while True:
    print("\nMENÚ DE INVENTARIO")
    print("1. Agregar producto")
    print("2. Actualizar stock")
    print("3. Buscar producto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        codigo = input("Ingrese el código: ")

        if codigo in inventario:
            print("El producto ya existe.")
        else:
            nombre = input("Ingrese el nombre: ")
            precio = float(input("Ingrese el precio: "))
            cantidad = int(input("Ingrese la cantidad: "))

            if precio < 0 or cantidad < 0:
                print("El precio y la cantidad no pueden ser negativos.")
            else:
                inventario[codigo] = {
                    "nombre": nombre,
                    "precio": precio,
                    "stock": cantidad
                }
                print("Producto agregado correctamente.")

    elif opcion == "2":
        codigo = input("Ingrese el código: ")

        if codigo in inventario:
            cantidad = int(input("Ingrese el nuevo stock: "))
            if cantidad >= 0:
                inventario[codigo]["stock"] = cantidad
                print("Stock actualizado.")
            else:
                print("El stock no puede ser negativo.")
        else:
            print("Producto no encontrado.")

    elif opcion == "3":
        codigo = input("Ingrese el código: ")

        if codigo in inventario:
            print("Nombre:", inventario[codigo]["nombre"])
            print("Precio:", inventario[codigo]["precio"])
            print("Stock:", inventario[codigo]["stock"])
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción incorrecta.")
