# Ejercicio 13 (Bingo)
from collections import deque
import random
from typing import Deque, List


def armar_secuencia_bingo() -> Deque[int]:
    """
    Devuelve una cola con los números 0..99 en orden aleatorio sin repetidos.
    """
    numeros = list(range(100))
    random.shuffle(numeros)
    return deque(numeros)


def jugar_carton_bingo(carton: List[int], bolillero: Deque[int]) -> int:
    """
    Dado carton (lista de 12 números únicos entre 0 y 99) y bolillero (cola con 100 números 0..99 en orden aleatorio),
    retorna la cantidad mínima de jugadas necesarias para que todos los números del cartón salgan.
    No modifica bolillero original (trabaja con copia).
    """
    if len(carton) != 12:
        raise ValueError("carton debe tener 12 numeros")
    if len(set(carton)) != 12:
        raise ValueError("carton no debe tener repetidos")
    bcopy = deque(bolillero)
    encontrados = set()
    jugadas = 0
    while bcopy and len(encontrados) < 12:
        num = bcopy.popleft()
        jugadas += 1
        if num in carton:
            encontrados.add(num)
    return jugadas
