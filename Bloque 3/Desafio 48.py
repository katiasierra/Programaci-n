class Libro:
    def __init__(self, titulo, genero, isbn, autor):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = autor

    def mostrar_libro(self):
        print("Título:", self.titulo)
        print("Género:", self.genero)
        print("ISBN:", self.isbn)
        print("Autor:", self.autor.nombre)


class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    # Agrega un libro a la lista del autor
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Elimina un libro de la lista
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print("Libro eliminado:", libro.titulo)
        else:
            print("El libro no está en la lista")

    # Muestra los datos del autor y sus libros
    def mostrar_autor(self):
        print("Autor:", self.nombre)
        print("Libros escritos:")

        for libro in self.libros:
            print("-", libro.titulo)


# Creo un autor
autor1 = Autor("Roy Berocay")

# Creo los libros
libro1 = Libro(
    "Pateando lunas",
    "Literatura infantil",
    "ISBN 001",
    autor1
)

libro2 = Libro(
    "El sapo Ruperto",
    "Literatura infantil",
    "ISBN 002",
    autor1
)

# Agrego los libros al autor
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)

# Muestro el autor y sus libros
autor1.mostrar_autor()

# Muestro los datos de un libro
print()
libro1.mostrar_libro()

# Elimino un libro
print()
autor1.eliminar_libro(libro2)

# Muestro nuevamente los libros del autor
print()
autor1.mostrar_autor()
