class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn


class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo):
        super().__init__(titulo, autor, isbn)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("ISBN:", self.isbn)
        print("Formato:", self.formato)
        print("Tamaño del archivo:", self.tamaño_archivo)


class EBook(LibroDigital):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo, enlace_descarga):
        super().__init__(titulo, autor, isbn, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Enlace de descarga:", self.enlace_descarga)


# Crear un LibroDigital
libro_digital = LibroDigital(
    "Pateando Lunas",
    "Roy Berocay",
    "978-9974-123-45-6",
    "PDF",
    "5 MB"
)

# Crear un EBook
ebook = EBook(
    "El sapo Ruperto",
    "Roy Berocay",
    "978-9974-456-78-9",
    "EPUB",
    "3 MB",
    "www.biblioteca.com/ruperto"
)


print("LIBRO DIGITAL")
libro_digital.mostrar_informacion()

print("\nEBOOK")
ebook.mostrar_informacion()
