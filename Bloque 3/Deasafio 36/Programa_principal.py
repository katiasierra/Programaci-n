"""Programa que utiliza el módulo personalizado formato_texto."""

import formato_texto
def mostrar_formatos(texto):
    """Muestra el texto utilizando diferentes formatos."""
    print("\nResultados:")
    print("Texto normal:", texto)
    print("Negrita:", formato_texto.negrita(texto))
    print("Itálica:", formato_texto.italica(texto))
    print("Subrayado:", formato_texto.subrayado(texto))
    print("Color azul:", formato_texto.color_azul(texto))
    print(
        "Negrita y subrayado:",
        formato_texto.negrita_subrayado(texto),
    )


def main():
    """Solicita un texto al usuario y muestra sus formatos."""
    texto_usuario = input("Ingrese un texto: ")
    mostrar_formatos(texto_usuario)


if __name__ == "__main__":
    main()
