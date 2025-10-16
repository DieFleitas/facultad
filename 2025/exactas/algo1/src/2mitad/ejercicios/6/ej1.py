import math


def imprimir_hola_mundo() -> None:
    """Imprime 'Hola mundo!' por consola."""
    print("Hola mundo!")


def imprimir_un_verso() -> None:
    """Imprime un verso con saltos de linea usando '\n'."""
    verso: str = "En el silencio de la noche,\nla luna canta su canción."
    print(verso)


def raizDe2() -> float:
    """Devuelve la raiz cuadrada de 2 redondeada a 4 decimales."""
    return round(math.sqrt(2), 4)


def factorial_de_dos() -> int:
    """Devuelve 2!"""
    return 2  # trivial, 2! = 2


def perimetro() -> float:
    """Devuelve el perimetro de la circunferencia de radio 1: 2*pi."""
    return 2 * math.pi
