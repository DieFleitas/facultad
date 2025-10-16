def alguno_es_0(numero1: float, numero2: float) -> bool:
    """Devuelve True si alguno de los dos es 0."""
    return (numero1 == 0) or (numero2 == 0)


def ambos_son_0(numero1: float, numero2: float) -> bool:
    """Devuelve True si ambos son 0."""
    return (numero1 == 0) and (numero2 == 0)


def es_nombre_largo(nombre: str) -> bool:
    """True si 3 <= len(nombre) <= 8."""
    l: int = len(nombre)
    return (3 <= l) and (l <= 8)


def es_bisiesto(anio: int) -> bool:
    """Devuelve True si el año es bisiesto según reglas gregorianas."""
    return (es_multiplo_de(anio, 400)) or (
        es_multiplo_de(anio, 4) and not es_multiplo_de(anio, 100)
    )
