class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre.strip() == "":
            print("Error: el nombre no puede estar vacío.")
        else:
            self.__nombre = nuevo_nombre

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        if nueva_nacionalidad.strip() == "":
            print("Error: la nacionalidad no puede estar vacía.")
        else:
            self.__nacionalidad = nueva_nacionalidad


# Crear un objeto Autor
autor1 = Autor("J. K. Rowling", "Británica")

# Mostrar sus datos usando las propiedades
print("Nombre:", autor1.nombre)
print("Nacionalidad:", autor1.nacionalidad)

# Modificar los datos utilizando los setter
autor1.nombre = "Joanne Rowling"
autor1.nacionalidad = "Inglesa"

print("\nDatos modificados:")
print("Nombre:", autor1.nombre)
print("Nacionalidad:", autor1.nacionalidad)

# Intentar asignar valores vacíos
autor1.nombre = ""
autor1.nacionalidad = ""

# Comprobar que se conservaron los valores anteriores
print("\nDatos después de intentar asignar valores vacíos:")
print("Nombre:", autor1.nombre)
print("Nacionalidad:", autor1.nacionalidad)
