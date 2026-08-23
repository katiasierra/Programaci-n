# TAD Biblioteca

biblioteca = []


# Función para agregar un libro
def agregar_libro(titulo):
    biblioteca.append(titulo)
    print("Libro agregado:", titulo)


# Función para eliminar un libro
def eliminar_libro(titulo):
    if titulo in biblioteca:
        biblioteca.remove(titulo)
        print("Libro eliminado:", titulo)
    else:
        print("El libro no se encuentra en la biblioteca.")


# Función para buscar un libro
def buscar_libro(titulo):
    if titulo in biblioteca:
        print("El libro", titulo, "está disponible.")
    else:
        print("El libro", titulo, "no está disponible.")


# Función para mostrar todos los libros
def mostrar_libros():
    print("Libros disponibles:")

    for libro in biblioteca:
        print("-", libro)


# Prueba del programa

agregar_libro("Pateando Lunas")
agregar_libro("El sapo Ruperto")
agregar_libro("1930: el viaje")
agregar_libro("Harry Potter")

print()

mostrar_libros()

print()

buscar_libro("Harry Potter")

print()

eliminar_libro("El sapo Ruperto")

print()

mostrar_libros()
