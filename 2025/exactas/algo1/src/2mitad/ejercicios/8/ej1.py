# Ejercicio 1
from random import random
from typing import List


def generar_nros_azar_pila(cantidad: int, desde: int, hasta: int) -> List[int]:
    """
    Genera una pila (lista) con 'cantidad' números aleatorios enteros uniformes en [desde, hasta].
    Pre: cantidad >= 0, desde <= hasta.
    Post: devuelve lista con length == cantidad, elementos en rango.
    """
    if cantidad < 0:
        raise ValueError("cantidad debe ser >= 0")
    if desde > hasta:
        raise ValueError("desde <= hasta")
    pila: List[int] = []
    i = 0
    while i < cantidad:
        pila.append(random.randint(desde, hasta))
        i += 1
    return pila
