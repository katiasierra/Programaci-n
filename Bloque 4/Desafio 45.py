# Desafío 45: Dos bibliotecas, un mismo TAD

biblioteca1 = []
biblioteca2 = []


# Función para agregar un libro
def agregar(biblioteca, titulo):
    biblioteca.append(titulo)
    print("Libro agregado:", titulo)


# Función para eliminar un libro
def eliminar(biblioteca, titulo):
    if titulo in biblioteca:
        biblioteca.remove(titulo)
        print("Libro eliminado:", titulo)
    else:
        print("El libro no se encuentra en la biblioteca.")


# Función para buscar un libro
def buscar(biblioteca, titulo):
    if titulo in biblioteca:
        print("El libro", titulo, "está disponible.")
    else:
        print("El libro", titulo, "no está disponible.")


# Función para mostrar los libros
def mostrar(biblioteca):
    for libro in biblioteca:
        print("-", libro)


# Agregamos libros a la biblioteca 1
agregar(biblioteca1, "Pateando Lunas")
agregar(biblioteca1, "El sapo Ruperto")

# Agregamos libros a la biblioteca 2
agregar(biblioteca2, "1930: el viaje")
agregar(biblioteca2, "Harry Potter")


print("\nBiblioteca 1:")
mostrar(biblioteca1)

print("\nBiblioteca 2:")
mostrar(biblioteca2)


# Realizamos una búsqueda
print("\nBúsqueda:")
buscar(biblioteca1, "Pateando Lunas")


# Eliminamos un libro
print("\nEliminación:")
eliminar(biblioteca2, "Harry Potter")


# Mostramos nuevamente ambas bibliotecas
print("\nContenido final de la Biblioteca 1:")
mostrar(biblioteca1)

print("\nContenido final de la Biblioteca 2:")
mostrar(biblioteca2)
