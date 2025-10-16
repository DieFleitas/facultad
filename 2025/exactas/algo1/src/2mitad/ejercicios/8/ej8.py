# Ejercicio 8
from collections import deque
from random import random
from typing import Deque


def generar_nros_azar_cola(cantidad: int, desde: int, hasta: int) -> Deque[int]:
    """
    Genera una cola con 'cantidad' números uniformes en [desde,hasta].
    Pre: cantidad >= 0, desde <= hasta.
    """
    if cantidad < 0:
        raise ValueError("cantidad >= 0")
    if desde > hasta:
        raise ValueError("desde <= hasta")
    c: Deque[int] = deque()
    i = 0
    while i < cantidad:
        c.append(random.randint(desde, hasta))
        i += 1
    return c
