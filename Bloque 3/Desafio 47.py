class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # Lista donde se guardan los libros del autor

    # Método para agregar un libro
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print("Libro agregado:", libro)

    # Método para eliminar un libro
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print("Libro eliminado:", libro)
        else:
            print("El libro no se encuentra en la lista")

    # Método para mostrar los libros
    def mostrar_libros(self):
        print("Libros de", self.nombre + ":")
        for libro in self.libros:
            print("-", libro)


# Creo un autor
autor1 = Autor("Roy Berocay")

# Agrego libros
autor1.agregar_libro("Pateando lunas")
autor1.agregar_libro("El sapo Ruperto")
autor1.agregar_libro("Ruperto y los extraterrestres")

# Muestro los libros
autor1.mostrar_libros()

# Elimino un libro
autor1.eliminar_libro("El sapo Ruperto")

# Muestro nuevamente la lista
autor1.mostrar_libros()
