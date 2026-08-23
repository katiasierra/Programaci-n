"""Funciones para aplicar formatos de texto."""
def negrita(texto):
    """Devuelve el texto en negrita."""
    return "\033[1m" + texto + "\033[0m"
def italica(texto):
    """Devuelve el texto en itálica."""
    return "\033[3m" + texto + "\033[0m"
def subrayado(texto):
    """Devuelve el texto subrayado."""
    return "\033[4m" + texto + "\033[0m"
def color_azul(texto):
    """Devuelve el texto en color azul."""
    return "\033[34m" + texto + "\033[0m"
def negrita_subrayado(texto):
    """Devuelve el texto en negrita y subrayado."""
    return "\033[1;4m" + texto + "\033[0m"
